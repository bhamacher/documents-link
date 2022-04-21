import unittest
import os
from database import TextFile_database


class Test(unittest.TestCase):

    def setUp(self):
        self.request = TextFile_database.databaseOpenRequest()
        self.db = TextFile_database.TextFileDatabase()
        self.path = "/s-zera-stor01/File3.docx"
        return super().setUp()

    def test_OpenDatabase(self):
        self.assertTrue(self.db.open(self.request))
    
    def test_OpenDatabaseWithWrongTypeThrowsException(self):
        with self.assertRaises(ValueError) as context:
            request="/file/path/file.txt"
            self.assertTrue(self.db.open(request))
        the_exception = context.exception
        self.assertTrue("Invalid database type" in the_exception.args)
    
    def test_IsOpenReturnsFalse(self):
        self.assertFalse(self.db.isOpen())

    def test_IsOpenReturnsTrueWhenDatabaseOpenWasCalled(self):
        OpenWasCalled = self.db.open(self.request)
        self.assertTrue(OpenWasCalled)
        self.assertTrue(self.db.isOpen())

    def test_CloseDatabase(self):
        self.assertTrue(self.db.close())

    def test_IsOpenReturnsFalseWhenDatabaseOpenAndCloseWasCalled(self):
        DatabaseOpen = self.db.open(self.request)
        self.assertTrue(DatabaseOpen)
        CloseWasCalled = self.db.close()
        self.assertTrue(CloseWasCalled)
        IsOpenReturnsFalse = self.db.isOpen()
        self.assertFalse(IsOpenReturnsFalse)

    def test_AddFilePathThrowsIfDatabaseIsNotOpen(self):
        with self.assertRaises(RuntimeError) as context:
            self.assertTrue(self.db.add_filePath("/path/"))
        the_exception = context.exception
        self.assertTrue("database is not open" in the_exception.args)

    def test_AddFilePathWhenDatabaseIsOpen(self):
        DatabaseIsOpen = self.db.open(self.request)
        self.assertTrue(DatabaseIsOpen)
        AddFilePath = self.db.add_filePath(self.path)
        self.assertEqual(AddFilePath, self.path)
    
    def test_RemoveFilePathThrowsIfDatabaseIsNotOpen(self):
        with self.assertRaises(RuntimeError) as context:
            self.assertTrue(self.db.remove_filePath("/path/"))
        the_exception = context.exception
        self.assertTrue("database is not open" in the_exception.args)

###############

    def test_ContainsFileTruePathWhenDatabaseOpen(self):
        DatabaseOpen = self.db.open(self.request)
        self.assertTrue(DatabaseOpen)
        ContainsFileTrue = self.db.contains_filePath(self.path)
        self.assertTrue(ContainsFileTrue)

    def test_ContainsFilePathThrowsIfDatabaseIsNotOpen(self):
        with self.assertRaises(RuntimeError) as context:
            self.assertTrue(self.db.contains_filePath("/path/"))
        the_exception = context.exception
        self.assertTrue("database is not open" in the_exception.args)

    def test_GetAllFilePathTruePathWhenDatabaseOpen(self):
        DatabaseOpen = self.db.open(self.request)
        self.assertTrue(DatabaseOpen)
        ContainsFileTrue = self.db.get_all_Path()
        self.assertEqual(type(ContainsFileTrue), list)

    def test_GetAllFilePathThrowsIfDatabaseIsNotOpen(self):
        with self.assertRaises(RuntimeError) as context:
            self.assertTrue(self.db.get_all_Path())
        the_exception = context.exception
        self.assertTrue("database is not open" in the_exception.args)




if __name__ == '__main__':
    unittest.main(verbosity=2)
