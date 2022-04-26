import unittest
import os
import shutil
from os import path
import tempfile
from zipfile import ZipFile
from document_links import file_unpacking

def test_link_data():
    return os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'test_link_data'))


docx_file_path_zip = os.path.join(test_link_data(), "TestLinkJenkins.docx")
xlsx_folder_path_zip = os.path.join(test_link_data(), "neuerJenkins.xlsx")

class Test(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.gettempdir()  # Generate temporary directory as temp_dir for unzipping files

    def tearDown(self):
        try: # Delete temp files.
            if path.isdir(self.temp_dir):
                shutil.rmtree(self.temp_dir, ignore_errors=True)
        except OSError as error:
            print("Error: %s - %s." % (error.filename, error.strerror))

    def test_1_archive_file_path_invalid(self):
        file_path_object = file_unpacking.FilePathValidation()
        success = file_path_object.path_valid_file("datei_name.foo", test_link_data())
        self.assertEqual(success, False)

    def test_2_destination_path_invalid(self):
        file_path_object = file_unpacking.FilePathValidation()
        success = file_path_object.path_valid_file(os.path.join(test_link_data(), "TestLinkJenkins.docx"), "filename.foo")
        self.assertEqual(success, False)

    def test_3_valid_both(self):
        file_path_object = file_unpacking.FilePathValidation()
        success = file_path_object.path_valid_file(os.path.join(test_link_data(), "TestLinkJenkins.docx"), test_link_data())
        self.assertEqual(success, True)

    def test_4_unzip_docx_file_found(self):
        ZipFile(docx_file_path_zip).extractall(self.temp_dir)
        self.assertEqual(os.path.isfile(os.path.join(self.temp_dir, "[Content_Types].xml")), True)

    def test_5_unzip_docx_folder_found(self):
        ZipFile(docx_file_path_zip).extractall(self.temp_dir)
        self.assertEqual(os.path.isdir(os.path.join(self.temp_dir, "docProps")), True)

    def test_6_unzip_xlsx_file_found(self):
        ZipFile(xlsx_folder_path_zip).extractall(self.temp_dir)
        self.assertEqual(os.path.isfile(os.path.join(self.temp_dir, "[Content_Types].xml")), True)

    def test_7_unzip_xlsx_folder_found(self):
        ZipFile(xlsx_folder_path_zip).extractall(self.temp_dir)
        self.assertEqual(os.path.isdir(os.path.join(self.temp_dir, "docProps")), True)


if __name__ == '__main__':
    unittest.main(verbosity=2)
