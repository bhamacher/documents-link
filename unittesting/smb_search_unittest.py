import unittest
import shutil
from os import path
import tempfile
from modules import smb_search

smb_data_source = "smb://s-zera-stor01/data1/Mitarbeiter/test_link_data"

class Test(unittest.TestCase):

    def test_1_found_files_xlsx(self):
        file_path_object = smb_search.SmbSearch()
        success = file_path_object.smb_search_file(smb_data_source, "*.xlsx")
        print("\nTotal .xlsx found:  -->", success)
        self.assertTrue(success)

    def test_2_found_files_docx(self):
        file_path_object = smb_search.SmbSearch()
        success = file_path_object.smb_search_file(smb_data_source, "*.docx")
        print("\nTotal .docx found: -->", success)
        self.assertTrue(success)

    def test_3_found_files_lnk(self):
        file_path_object = smb_search.SmbSearch()
        success = file_path_object.smb_search_file(smb_data_source, "*.lnk")
        print("\nTotal .lnk found: -->", success)
        self.assertTrue(success)


if __name__ == '__main__':
    unittest.main(verbosity=2)
