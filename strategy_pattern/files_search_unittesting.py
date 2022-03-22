import unittest
import os
import files_search
import smb_search
import local_search

## local
TESTDIR_STRUCTURE = [
    'folder1/foo1.txt',
    'folder11/text11.txt',
    'folder11/text11a.txt',
    'folder12/text21.txt',
    'folder12/text21a.txt',
    'folder2/foo2.txt',
    'folder21/text21.txt',
    'folder22/text22.txt']

def test_folder():
    return os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'test_folder'))

## smb
smb_data = "smb://s-zera-stor01/data1/Mitarbeiter/test_link_data"

class Test(unittest.TestCase):

### local_search
    def test_1_local_search_invalid_path(self):
        file_path_object = files_search.FileSearch(local_search.LocalFileSearch())
        search_result = file_path_object.search_file_strategy("path_foo", ["*.txt"])
        self.assertIs(search_result, None)

    def test_2_local_search_valid_path(self):
        file_path_object = files_search.FileSearch(local_search.LocalFileSearch())
        search_result = file_path_object.search_file_strategy(test_folder(), ["*.foo"])
        self.assertIs(len(search_result), 0)

    def test_3_local_search_found_files_txt(self):
        file_path_object = files_search.FileSearch(local_search.LocalFileSearch())
        search_result = file_path_object.search_file_strategy(test_folder(), ["*.txt"])
        self.assertEqual(len(search_result), len(TESTDIR_STRUCTURE))

    def test_4_local_search_files_found_doc(self):
        file_path_object = files_search.FileSearch(local_search.LocalFileSearch())
        search_result = file_path_object.search_file_strategy(test_folder(), ["*.doc"])
        self.assertEqual(len(search_result), 1)

    def test_5_local_search_files_found_doc_and_text(self):
        file_path_object = files_search.FileSearch(local_search.LocalFileSearch())
        search_result = file_path_object.search_file_strategy(test_folder(), ["*.doc", "*.txt"])
        self.assertEqual(len(search_result), len(TESTDIR_STRUCTURE)+1)

    def test_6_local_search_files_found_win_path(self):
        file_path_object = files_search.FileSearch(local_search.LocalFileSearch())
        search_path = (test_folder().replace('/', '\\'))
        search_result = file_path_object.search_file_strategy(search_path, ["*.txt"])
        self.assertEqual(len(search_result), len(TESTDIR_STRUCTURE))

    def test_7_local_search_files_found_linux_path(self):
        file_path_object = files_search.FileSearch(local_search.LocalFileSearch())
        search_path = (test_folder().replace('\\', '/'))
        search_result = file_path_object.search_file_strategy(search_path, ["*.txt"])
        self.assertEqual(len(search_result), len(TESTDIR_STRUCTURE))

### smb_search
    def test_1_smb_search_found_files_xlsx(self):
        file_path_object = files_search.FileSearch(smb_search.SmbSearch())
        success = file_path_object.search_file_strategy(smb_data, "*.xlsx")
        self.assertTrue(success)

    def test_2_smb_search_found_files_docx(self):
        file_path_object = files_search.FileSearch(smb_search.SmbSearch())
        success = file_path_object.search_file_strategy(smb_data, "*.docx")
        self.assertTrue(success)

    def test_3_smb_search_found_files_lnk(self):
        file_path_object = files_search.FileSearch(smb_search.SmbSearch())
        success = file_path_object.search_file_strategy(smb_data, "*.lnk")
        self.assertTrue(success)


if __name__ == '__main__':
    unittest.main(verbosity=2)
