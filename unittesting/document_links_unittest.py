import unittest
import os
import sys
from document_links import document_links


def test_link_data():
    return os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'test_folder'))


class Test(unittest.TestCase):


    def test_1_update_filetable(self):
        file_path_object = document_links.DocumentLinks()
        update_filetable = file_path_object.update_filetable(test_link_data())
        self.assertTrue(update_filetable)

    def test_2_clean_filetable(self):
        file_path_object = document_links.DocumentLinks()
        clean_filetable = file_path_object.clean_filetable("")
        self.assertTrue(clean_filetable)

if __name__ == '__main__':
    unittest.main(verbosity=2)