import unittest
import os
from document_links import local_copy_file


def test_link_data():
    return os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'test_link_data'))

docx_file_path_zip = os.path.join(test_link_data(), "TestLinkJenkins.docx")

class Test(unittest.TestCase):

    def setUp(self) -> None:
        self.file_path_object = local_copy_file.LocalCopyFile()
        return super().setUp()

    def test_1_local_copy_file_unittest(self):
        user_name           = " "
        password            = " "
        destination         = " "
        search_result = self.file_path_object.copy_file(docx_file_path_zip, destination, user_name, password)
        self.assertIsNotNone(search_result)


if __name__ == '__main__':
    unittest.main(verbosity=2)