import tempfile
import os
import re
import shutil
from zipfile import ZipFile
from pathlib import Path
import xml.etree.ElementTree as ET
from document_links import I_copy_file

def FileTable():
    return os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'test_folder','txt_file_database_test',"FileTable.txt"))

def InvalidLinks():
    return os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'test_folder','txt_file_database_test',"InvalidLinks.txt"))

def output_zip():
    return os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', "test_folder", "output_zip"))


class LocalCopyFile(I_copy_file.ICopyFileStrategy):

    def copy_file(self, source, destination, user_name, password):
        if not "smb://" in source:
            destination = tempfile.gettempdir()
            shutil.copy(source, destination)
            base_file_name = Path(source).name
            tmp_file = os.path.join(destination, base_file_name)
            search_result = []

            ZipFile(tmp_file).extractall(output_zip())
            xml_file = os.path.join(output_zip() + "/word" + "/document.xml")
            print("---> 1", xml_file)
            sub_string = "s-zera"
            root = ET.parse(xml_file).getroot()
            iteration_elements = root.iter()
            for elem in iteration_elements:
                if sub_string in str(elem.text):
                    print("---> 2", elem.text)
                    data_link = (elem.text).replace('\\', '/') # change window path to smb path.
                    if "HYPERLINK" in data_link:
                            data_link = data_link.replace('//', '/')
                            data_link = (re.findall('\"([^"]*)\"', data_link))[0] # to remove text "HYPERLINK" from string.
                    linux_data_path = 'smb:' + data_link 
                    with open(FileTable()) as f:
                            if not linux_data_path in str([line.rstrip('\n') for line in f]):
                                search_result.append(linux_data_path)

            return search_result
        else:
            return False
