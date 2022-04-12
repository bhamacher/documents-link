import unittest
from modules import smb_search

smb_data = "smb://s-zera-stor01/data1/Zusammenarbeit/Transferordner/EW/DKU"

class Test(unittest.TestCase):

    def setUp(self) -> None:
        self.file_path_object = smb_search.SmbSearch()
        return super().setUp()

### smb_search
    def test_8_smb_search_found_files_xlsx(self):
        success = self.file_path_object.search_file(smb_data, "*.xlsx")
        self.assertTrue(success)

    def test_9_smb_search_found_files_docx(self):
        success = self.file_path_object.search_file(smb_data, "*.docx")
        self.assertTrue(success)

    def test_10_smb_search_found_files_lnk(self):
        success = self.file_path_object.search_file(smb_data, "*.lnk")
        self.assertTrue(success)


if __name__ == '__main__':
    unittest.main(verbosity=2)
