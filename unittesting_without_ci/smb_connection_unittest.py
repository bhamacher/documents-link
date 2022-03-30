import unittest
import os, sys
from urllib.parse import urlparse

script_dir = os.path.dirname( __file__ )
mymodule_dir = os.path.join( script_dir, '..', 'modules')
sys.path.append(mymodule_dir)
import smb_connection

## smb
smb_data_path = "smb://s-zera-stor01/data1/Zusammenarbeit/Transferordner/EW/DKU"
server_name = urlparse(smb_data_path).netloc


class Test(unittest.TestCase):

    def test_1_connection(self):
        smb_path_connection = smb_connection.SmbServerConnection()
        connection = smb_path_connection.get_connection(server_name)
        self.assertIsNotNone(connection)

    def test_2_connects_one_credential(self):
        smb_path_connection = smb_connection.SmbServerConnection()
        connection = smb_path_connection.get_connection(server_name)
        self.assertIsNotNone(connection)
        connection1 = smb_path_connection.get_connection(server_name)
        self.assertIsNotNone(connection1)
        self.assertEqual(smb_path_connection.get_connection_count(), 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
