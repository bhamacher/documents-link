import unittest
from getpass import getpass
from modules import local_copy_file

data_full_path = "/home/d.kumar/Desktop/working/documents-link/test_link_data/file_1.docx"

class Test(unittest.TestCase):

    def setUp(self) -> None:
        self.file_path_object = local_copy_file.LocalCopyFile()
        return super().setUp()

    def test_1_smb_copy_file_unittest(self):
        user_name           = " "
        password            = " "
        destination         = " "
        search_result = self.file_path_object.copy_file(data_full_path, destination, user_name, password)
        self.assertEqual(search_result, True)

    

if __name__ == '__main__':
    unittest.main(verbosity=2)