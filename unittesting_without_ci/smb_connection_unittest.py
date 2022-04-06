import unittest
import os, sys
from urllib.parse import urlparse

script_dir = os.path.dirname( __file__ )
mymodule_dir = os.path.join( script_dir, '..', 'modules')
sys.path.append(mymodule_dir)
import smb_connection

## smb
smb_path_name = "smb://s-zera-stor01/data1/Zusammenarbeit/Transferordner/EW/DKU/test_link_data/docx_data/Abt-TB-2021-05-03.docx"


class Test(unittest.TestCase):

    def test_1_connection(self):
        smb_path_connection = smb_connection.SmbServerConnectionHandler()
        connection = smb_path_connection.get_connection(smb_path_name)
        self.assertIsNotNone(connection)

    def test_2_connects_one_credential(self):
        smb_path_connection = smb_connection.SmbServerConnectionHandler()
        connection = smb_path_connection.get_connection(smb_path_name)
        self.assertIsNotNone(connection)
        self.assertEqual(smb_path_connection.get_connection_count(), 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
