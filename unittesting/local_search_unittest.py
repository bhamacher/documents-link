import unittest
import os
from modules import local_search

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

class Test(unittest.TestCase):
    def test_invalid_path(self):
        file_search_object = local_search.LocalFileSearch()
        search_result = file_search_object.local_search_file("path_foo", ["*.txt"])
        self.assertIs(search_result, None)

    def test_valid_path(self):
        file_search_object = local_search.LocalFileSearch()
        search_result = file_search_object.local_search_file(test_folder(), ["*.foo"])
        self.assertIs(len(search_result), 0)

    def test_files_found(self):
        file_search_object = local_search.LocalFileSearch()
        search_result = file_search_object.local_search_file(test_folder(), ["*.txt"])
        self.assertEqual(len(search_result), len(TESTDIR_STRUCTURE))

    def test_files_found_doc(self):
        file_search_object = local_search.LocalFileSearch()
        search_result = file_search_object.local_search_file(test_folder(), ["*.doc"])
        self.assertEqual(len(search_result), 1)

    def test_files_found_doc_and_text(self):
        file_search_object = local_search.LocalFileSearch()
        search_result = file_search_object.local_search_file(test_folder(), ["*.doc", "*.txt"])
        self.assertEqual(len(search_result), len(TESTDIR_STRUCTURE)+1)

    def test_files_found_win_path(self):
        file_search_object = local_search.LocalFileSearch()
        search_path = (test_folder().replace('/', '\\'))
        search_result = file_search_object.local_search_file(search_path, ["*.txt"])
        self.assertEqual(len(search_result), len(TESTDIR_STRUCTURE))

    def test_files_found_linux_path(self):
        file_search_object = local_search.LocalFileSearch()
        search_path = (test_folder().replace('\\', '/'))
        search_result = file_search_object.local_search_file(search_path, ["*.txt"])
        self.assertEqual(len(search_result), len(TESTDIR_STRUCTURE))

if __name__ == '__main__':
    unittest.main(verbosity=2)
