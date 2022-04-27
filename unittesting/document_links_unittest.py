import unittest
import os
import sys
from document_links import document_links
from unittesting.spy.db_spy import db_spy


def test_link_data():
    return os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'test_folder'))


class Test(unittest.TestCase):

    def setUp(self) -> None:
        self.db = db_spy()
        self.path='/home/bhamacher/workspace/documents-link/test_folder/folder_test'
        return super().setUp()

    def test_1_update_filetable(self):
        file_path_object = document_links.DocumentLinks(self.db)
        update_filetable = file_path_object.update_filetable([self.path])
        self.assertTrue(update_filetable)
        expectedResult={'/home/bhamacher/workspace/documents-link/test_folder/folder_test/notfound/nichtexit.doc',
        '/home/bhamacher/workspace/documents-link/test_folder/folder_test/folder12/text21a.txt',
        '/home/bhamacher/workspace/documents-link/test_folder/folder_test/folder12/text21.txt',
        '/home/bhamacher/workspace/documents-link/test_folder/folder_test/folder11/text11.txt',
        '/home/bhamacher/workspace/documents-link/test_folder/folder_test/folder2/folder21', 
        '/home/bhamacher/workspace/documents-link/test_folder/folder_test/folder11/text11a.txt',
        '/home/bhamacher/workspace/documents-link/test_folder/folder_test/folder2/folder21/text21.txt',
        '/home/bhamacher/workspace/documents-link/test_folder/folder_test/folder2/foo2.txt',
        '/home/bhamacher/workspace/documents-link/test_folder/folder_test/folder2/folder22',
        '/home/bhamacher/workspace/documents-link/test_folder/folder_test/folder2/folder22/text22.txt',
        '/home/bhamacher/workspace/documents-link/test_folder/folder_test/folder1/foo1.txt'}
        self.assertEqual(expectedResult,self.db.fileTable)

    # def test_2_clean_filetable(self):
    #     file_path_object = document_links.DocumentLinks(self.db)
    #     clean_filetable = file_path_object.clean_filetable([""])
    #     self.assertTrue(clean_filetable)

if __name__ == '__main__':
    unittest.main(verbosity=2)