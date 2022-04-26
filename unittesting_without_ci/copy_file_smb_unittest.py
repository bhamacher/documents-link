import unittest
from getpass import getpass
from document_links import smb_copy_file

smb_data_full_path = input("give smb data full path" + "\n" + "Example for smb : smb://s-zera-stor01/data1/dir/file.docx" + "\n")

class Test(unittest.TestCase):

    def setUp(self):
        self.file_path_object = smb_copy_file.SmbCopyFile()
        return super().setUp()

    def test_1_smb_copy_file_unittest(self):
        user_name           = getpass(prompt = 'Give your user_name: ')
        password            = getpass(prompt = 'Give your password: ')
        destination         = ""
        search_result = self.file_path_object.copy_file(smb_data_full_path, destination, user_name, password)
        self.assertIsNotNone(search_result)


if __name__ == '__main__':
    unittest.main(verbosity=2)
