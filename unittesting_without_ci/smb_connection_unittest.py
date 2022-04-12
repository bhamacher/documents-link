import unittest
from getpass import getpass
from modules import smb_connection

smb_path_name = "smb://s-zera-stor01/data1/Zusammenarbeit/Transferordner/EW/DKU/test_link_data/docx_data/Abt-TB-2021-05-03.docx"

class Test(unittest.TestCase):

    def test_1_connection(self):
        user_name           = getpass(prompt = 'Give your user_name: ')
        password            = getpass(prompt = 'Give your password: ')
        smb_path_connection = smb_connection.SmbServerConnectionHandler()
        connection = smb_path_connection.get_connection(smb_path_name, user_name, password)
        self.assertIsNotNone(connection)

    def test_2_connects_one_credential(self):
        user_name           = getpass(prompt = 'Give your user_name: ')
        password            = getpass(prompt = 'Give your password: ')
        smb_path_connection = smb_connection.SmbServerConnectionHandler()
        connection = smb_path_connection.get_connection(smb_path_name, user_name, password)
        self.assertIsNotNone(connection)
        self.assertEqual(smb_path_connection.get_connection_count(), 1)

    def test_3_no_connection(self):
        smb_path_connection = smb_connection.SmbServerConnectionHandler()
        connection = smb_path_connection.get_existing_connection()
        self.assertEqual(connection, 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
