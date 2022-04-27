import unittest
import os
import shutil
from document_links.database import TextFile_database

def FileTableCopy():
    return os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'test_folder','txt_file_database_test','tmp',"FileTable.txt"))

def InvalidLinksCopy():
    return os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'test_folder','txt_file_database_test','tmp',"InvalidLinks.txt"))

def FileTable():
    return os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'test_folder','txt_file_database_test',"FileTable.txt"))

def InvalidLinks():
    return os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'test_folder','txt_file_database_test',"InvalidLinks.txt"))

class Test(unittest.TestCase):

    def setUp(self):
        if os.path.isdir('test_folder/txt_file_database_test/tmp'):
            pass
        else:
            os.mkdir('test_folder/txt_file_database_test/tmp')
        shutil.copyfile(FileTable(), FileTableCopy())
        shutil.copyfile(InvalidLinks(), InvalidLinksCopy())
        self.request = TextFile_database.databaseProperties()
        self.request.text_file_database_name = FileTableCopy()
        self.request.invalid_link_database_name = InvalidLinksCopy()
        self.db = TextFile_database.TextFileDatabase(self.request)
        self.path = "/s-zera-stor01/File1.docx"
        self.link = "/s-zera-stor01/File_0.txt"
        return super().setUp()

    def tearDown(self):
        shutil.rmtree('test_folder/txt_file_database_test/tmp')
        return super().tearDown()

    def test_1_OpenDatabase(self):
        self.assertTrue(self.db.open())
    
    def test_2_CreateWithWrongTypeThrowsException(self):
        with self.assertRaises(ValueError) as context:
            request="/file/path/file.txt"
            TextFile_database.TextFileDatabase(request)
        the_exception = context.exception
        self.assertTrue("Invalid database type" in the_exception.args)
    
    def test_3_IsOpenReturnsFalse(self):
        self.assertFalse(self.db.isOpen())

    def test_4_IsOpenReturnsTrueWhenDatabaseOpenWasCalled(self):
        OpenWasCalled = self.db.open()
        self.assertTrue(OpenWasCalled)
        self.assertTrue(self.db.isOpen())

    def test_5_CloseDatabase(self):
        self.assertTrue(self.db.close())

    def test_6_IsOpenReturnsFalseWhenDatabaseOpenAndCloseWasCalled(self):
        DatabaseOpen = self.db.open()
        self.assertTrue(DatabaseOpen)
        CloseWasCalled = self.db.close()
        self.assertTrue(CloseWasCalled)
        IsOpenReturnsFalse = self.db.isOpen()
        self.assertFalse(IsOpenReturnsFalse)

    def test_7_AddFilePathThrowsIfDatabaseIsNotOpen(self):
        with self.assertRaises(RuntimeError) as context:
            self.assertTrue(self.db.add_filePath("/path/"))
        the_exception = context.exception
        self.assertTrue("database is not open" in the_exception.args)

    def test_8_AddFilePathWhenDatabaseIsOpen(self):
        DatabaseIsOpen = self.db.open()
        self.assertTrue(DatabaseIsOpen)
        AddFilePath = self.db.add_filePath(self.path)
        self.assertEqual(AddFilePath, self.path)
    
    def test_9_RemoveFilePathWhenDatabaseIsOpen(self):
        DatabaseIsOpen = self.db.open()
        self.assertTrue(DatabaseIsOpen)
        RemoveFilePath = self.db.remove_filePath(self.path)
        self.assertEqual(RemoveFilePath, self.path)
    
    def test_10_RemoveFilePathThrowsIfDatabaseIsNotOpen(self):
        with self.assertRaises(RuntimeError) as context:
            self.assertTrue(self.db.remove_filePath("/path/"))
        the_exception = context.exception
        self.assertTrue("database is not open" in the_exception.args)

    def test_11_ContainsFilePathWhenDatabaseOpenFileThere(self):
        DatabaseOpen = self.db.open()
        self.assertTrue(DatabaseOpen)
        ContainsFileTrue = self.db.contains_filePath(self.path)
        self.assertTrue(ContainsFileTrue)

    def test_12_ContainsFilePathWhenDatabaseOpenFileNotThere(self):
        DatabaseOpen = self.db.open()
        self.assertTrue(DatabaseOpen)
        ContainsFileFalse = self.db.contains_filePath("foo")
        self.assertFalse(ContainsFileFalse)

    def test_13_ContainsFilePathThrowsIfDatabaseIsNotOpen(self):
        with self.assertRaises(RuntimeError) as context:
            self.assertTrue(self.db.contains_filePath("/path"))
        the_exception = context.exception
        self.assertTrue("database is not open" in the_exception.args)

    def test_14_GetAllPathListPathWhenDatabaseOpen(self):
        DatabaseOpen = self.db.open()
        expected=[
            "/s-zera-stor01/File1.docx",
            "/s-zera-stor01/File2.docx",
            "/s-zera-stor01/File3.docx"
        ]
        self.assertTrue(DatabaseOpen)
        filelist = self.db.get_all_Path()
        self.assertEqual(filelist, expected)
        filelist = self.db.get_all_Path()
        self.assertEqual(filelist, expected)

    def test_15_GetAllPathThrowsIfDatabaseIsNotOpen(self):
        with self.assertRaises(RuntimeError) as context:
            self.assertTrue(self.db.get_all_Path())
        the_exception = context.exception
        self.assertTrue("database is not open" in the_exception.args)

    def test_16_AddInvalidLinkPathWhenDatabaseOpen(self):
        DatabaseOpen = self.db.open()
        self.assertTrue(DatabaseOpen)
        InvalidLink = self.db.add_invalidLink(self.path, self.link)
        self.assertEqual(InvalidLink, self.link)

    def test_17_AddInvalidLinkThrowsIfDatabaseIsNotOpen(self):
        with self.assertRaises(RuntimeError) as context:
            self.assertTrue(self.db.add_invalidLink("",""))
        the_exception = context.exception
        self.assertTrue("database is not open" in the_exception.args)

    def test_18_RemoveInvalidLinkWhenDatabaseOpen(self):
        DatabaseOpen = self.db.open()
        self.assertTrue(DatabaseOpen)
        InvalidLink = self.db.remove_invalidLink(self.path, self.link)
        self.assertEqual(InvalidLink, self.link)
        contains_invalidLin = self.db.contains_invalidLink(self.path, self.link)
        self.assertFalse(contains_invalidLin)
        get_invalid_links = self.db.get_invalid_links(self.path)
        self.assertNotIn(self.link, list(get_invalid_links))

    def test_19_RemoveInvalidLinkThrowsIfDatabaseIsNotOpen(self):
        with self.assertRaises(RuntimeError) as context:
            self.assertTrue(self.db.remove_invalidLink("",""))
        the_exception = context.exception
        self.assertTrue("database is not open" in the_exception.args)
   
    def test_20_ContainsInvalidLinkWhenDatabaseOpenLinkThere(self):
        DatabaseOpen = self.db.open()
        self.assertTrue(DatabaseOpen)
        ContainsFileTrue = self.db.contains_invalidLink(self.path, self.link)
        self.assertTrue(ContainsFileTrue)
    
    def test_21_ContainsInvalidLinkWhenDatabaseOpenLinkNotThere(self):
        DatabaseOpen = self.db.open()
        self.assertTrue(DatabaseOpen)
        ContainsFileFalse = self.db.contains_invalidLink(self.path, "foo")
        self.assertFalse(ContainsFileFalse)

    def test_22_ContainsInvalidLinkThrowsIfDatabaseIsNotOpen(self):
        with self.assertRaises(RuntimeError) as context:
            self.assertTrue(self.db.contains_invalidLink("/path","/link"))
        the_exception = context.exception
        self.assertTrue("database is not open" in the_exception.args)

    def test_23_GetInvalidLinksWhenDatabaseOpen(self):
        DatabaseOpen = self.db.open()
        self.assertTrue(DatabaseOpen)
        expected=set(
            [
                "/s-zera-stor01/File_0.txt"
            ]
        )
        invalidLinks = self.db.get_invalid_links(self.path)
        self.assertEqual(expected, invalidLinks)

    def test_24_GetInvalidLinkThrowsIfDatabaseIsNotOpen(self):
        with self.assertRaises(RuntimeError) as context:
            self.assertTrue(self.db.get_invalid_links("/path"))
        the_exception = context.exception
        self.assertTrue("database is not open" in the_exception.args)

    def test_25_GetAllInvalidLinkSetPathWhenDatabaseOpen(self):
        DatabaseOpen = self.db.open()
        self.assertTrue(DatabaseOpen)
        expected=set(
            [
                "/s-zera-stor01/File_0.txt",
                "/s-zera-stor01/File_1.txt"
            ]
        )
        invalidLinks= self.db.get_all_invalid_links()
        self.assertEqual(expected, invalidLinks)

    def test_26_GetAllInvalidLinksThrowsIfDatabaseIsNotOpen(self):
        with self.assertRaises(RuntimeError) as context:
            self.assertTrue(self.db.get_all_invalid_links())
        the_exception = context.exception
        self.assertTrue("database is not open" in the_exception.args)

    def test_27_RemoveAllOccurenceOfInvalidLinkWhenDatabaseOpen(self):
        DatabaseOpen = self.db.open()
        self.assertTrue(DatabaseOpen)
        InvalidLink = self.db.remove_all_occurence_of_invalid_link(self.link)
        self.assertEqual(InvalidLink, self.link)
        get_all_invalid_links = self.db.get_all_invalid_links()
        self.assertNotIn(self.link, list(get_all_invalid_links))
        get_invalid_links = self.db.get_invalid_links(self.path)
        self.assertNotIn(self.link, list(get_invalid_links))

    def test_28_RemoveAllOccurenceOfInvalidLinkThrowsIfDatabaseIsNotOpen(self):
        with self.assertRaises(RuntimeError) as context:
            self.assertTrue(self.db.remove_all_occurence_of_invalid_link(self.link))
        the_exception = context.exception
        self.assertTrue("database is not open" in the_exception.args)


if __name__ == '__main__':
    unittest.main(verbosity=2)