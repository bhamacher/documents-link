import tempfile
import os
import shutil
from zipfile import ZipFile
from pathlib import Path
import xml.etree.ElementTree as ET
from modules import I_copy_file


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
            sub_string = "s-zera-stor01"
            root = ET.parse(xml_file).getroot()
            iteration_elements = root.iter()
            for elem in iteration_elements:
                if sub_string in str(elem.text):
                    print("---> 2", elem.text)
    

            return True
        else:
            return False
