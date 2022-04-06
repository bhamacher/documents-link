import unittest
import os, sys
import tempfile
from os import path
import shutil
from urllib.parse import urlparse


# give path to "smb_path_to_local_path"
script_dir = os.path.dirname( __file__ )
mymodule_dir = os.path.join( script_dir, '..', 'modules')
sys.path.append(mymodule_dir)
import smb_path_to_local_path


smb_data_full_path = "smb://s-zera-stor01/data1/Zusammenarbeit/Transferordner/EW/DKU/test_link_data/docx_data/Besprechung_EWHardware_2022-02-01.docx"


class Test(unittest.TestCase):

    def test_1_smb_to_local(self):
        smb_path_connection = smb_path_to_local_path.FileToLocal()
        local_path = smb_path_connection.path_to_local(smb_data_full_path)
        self.assertEqual(local_path, True)
        

if __name__ == '__main__':
    unittest.main(verbosity=2)
