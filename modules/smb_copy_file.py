import os
import re
import time
import shutil
import xml.etree.ElementTree as ET
from zipfile import ZipFile
from urllib.parse import urlparse
from zipfile import ZipFile
from modules import smb_connection
import tempfile
from urllib.parse import urlparse
from modules import I_copy_file


def output_zip():
    return os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', "test_folder", "output_zip"))

def databank_smb():
    return os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', "test_folder", "databank_smb", "file.txt"))


class SmbCopyFile(I_copy_file.ICopyFileStrategy):

    def __init__(self):
        self.smbServerConnectionHandler = smb_connection.SmbServerConnectionHandler()
        pass

    def copy_file(self, source, destination, user_name, password):
        if "docx" in source:
            conn = self.smbServerConnectionHandler.get_connection(source, user_name, password)
            path_parse = urlparse(source)
            share_name = path_parse.path.split("/")[1]
            base_file_path = path_parse.path.split(share_name)[1]
            base_file_name = base_file_path.split("/")[-1]
            destination = tempfile.gettempdir() ## check for correct file.
            tmp_file = os.path.join(destination, base_file_name)
            search_result = []
            # download all_smb_file to databank
            with open(databank_smb(), 'wb') as fp_smb: # copy smb file to temp.
                conn.retrieveFile("data1", "/Zusammenarbeit/Transferordner/EW/DKU/databank_smb/all_smb_data_type.txt", fp_smb)
            time.sleep(5)
            with open(tmp_file, 'wb') as fp: # copy smb file to temp.
                conn.retrieveFile(share_name, base_file_path, fp)
                ZipFile(tmp_file).extractall(output_zip())
                xml_file = output_zip()+"/word/document.xml"
                sub_string = "s-zera-stor01"
                root = ET.parse(xml_file).getroot()
                iteration_elements = root.iter()
                for elem in iteration_elements:
                    if sub_string in str(elem.text):
                        data_link = (elem.text).replace('\\', '/') # change window path to smb path.
                        if "HYPERLINK" in data_link:
                                data_link = data_link.replace('//', '/')
                                data_link = (re.findall('\"([^"]*)\"', data_link))[0] # to remove HYPERLINK from string.
                        linux_data_path = 'smb:' + data_link 
                        with open(databank_smb()) as f:
                                if not linux_data_path in str([line.rstrip('\n') for line in f]):
                                    #print("\n" + "--->invalid_link: ", linux_data_path + "\n")
                                    search_result.append(linux_data_path)

            # delete databank_smb
            if os.path.exists(databank_smb()):
                os.remove(databank_smb())
            # delete all contents of output_zip
            shutil.rmtree(output_zip())

            if search_result == []:
                return "Not found Invalid link"
            else:
                return "Invalid link : " + str(search_result)

        else:
            return None
