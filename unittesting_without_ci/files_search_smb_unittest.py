import unittest
from modules import files_search
from modules import smb_search


## smb
smb_data = "smb://s-zera-stor01/data1/Mitarbeiter/test_link_data"

class Test(unittest.TestCase):

### smb_search
    def test_8_smb_search_found_files_xlsx(self):
        file_path_object = files_search.FileSearch(smb_search.SmbSearch())
        success = file_path_object.search_file_strategy(smb_data, "*.xlsx")
        self.assertTrue(success)

    def test_9_smb_search_found_files_docx(self):
        file_path_object = files_search.FileSearch(smb_search.SmbSearch())
        success = file_path_object.search_file_strategy(smb_data, "*.docx")
        self.assertTrue(success)

    def test_10_smb_search_found_files_lnk(self):
        file_path_object = files_search.FileSearch(smb_search.SmbSearch())
        success = file_path_object.search_file_strategy(smb_data, "*.lnk")
        self.assertTrue(success)


if __name__ == '__main__':
    unittest.main(verbosity=2)
