import unittest
from getpass import getpass
from modules import smb_copy_file

smb_data_full_path = "smb://s-zera-stor01/data1/Zusammenarbeit/Transferordner/EW/DKU/test_link_data/docx_data/Besprechung_EWHardware_2022-02-01.docx"


class Test(unittest.TestCase):

    def setUp(self) -> None:
        self.file_path_object = smb_copy_file.SmbCopyFile()
        return super().setUp()

    def test_1_smb_copy_file_unittest(self):
        user_name           = getpass(prompt = 'Give your user_name: ')
        password            = getpass(prompt = 'Give your password: ')
        destination         = ""
        search_result = self.file_path_object.copy_file(smb_data_full_path, destination, user_name, password)
        self.assertEqual(search_result, True)


if __name__ == '__main__':
    unittest.main(verbosity=2)
