import unittest
from database import TextFile_database

class Test(unittest.TestCase):

    def setUp(self):
        self.request = TextFile_database.databaseOpenRequest()
        self.db = TextFile_database.TextFileDatabase()
        self.path = "/s-zera-stor01/File3.docx"
        self.link = "/s-zera-stor01/File_0.txt"
        return super().setUp()

    def test_1_OpenDatabase(self):
        self.assertTrue(self.db.open(self.request))
    
    def test_2_OpenDatabaseWithWrongTypeThrowsException(self):
        with self.assertRaises(ValueError) as context:
            request="/file/path/file.txt"
            self.assertTrue(self.db.open(request))
        the_exception = context.exception
        self.assertTrue("Invalid database type" in the_exception.args)
    
    def test_3_IsOpenReturnsFalse(self):
        self.assertFalse(self.db.isOpen())

    def test_4_IsOpenReturnsTrueWhenDatabaseOpenWasCalled(self):
        OpenWasCalled = self.db.open(self.request)
        self.assertTrue(OpenWasCalled)
        self.assertTrue(self.db.isOpen())

    def test_5_CloseDatabase(self):
        self.assertTrue(self.db.close())

    def test_6_IsOpenReturnsFalseWhenDatabaseOpenAndCloseWasCalled(self):
        DatabaseOpen = self.db.open(self.request)
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
        DatabaseIsOpen = self.db.open(self.request)
        self.assertTrue(DatabaseIsOpen)
        AddFilePath = self.db.add_filePath(self.path)
        self.assertEqual(AddFilePath, self.path)
    
    def test_9_RemoveFilePathThrowsIfDatabaseIsNotOpen(self):
        with self.assertRaises(RuntimeError) as context:
            self.assertTrue(self.db.remove_filePath("/path/"))
        the_exception = context.exception
        self.assertTrue("database is not open" in the_exception.args)

    def test_10_ContainsFileTruePathWhenDatabaseOpen(self):
        DatabaseOpen = self.db.open(self.request)
        self.assertTrue(DatabaseOpen)
        ContainsFileTrue = self.db.contains_filePath(self.path)
        self.assertIn(ContainsFileTrue, [True, False])

    def test_11_ContainsFilePathThrowsIfDatabaseIsNotOpen(self):
        with self.assertRaises(RuntimeError) as context:
            self.assertTrue(self.db.contains_filePath("/path/"))
        the_exception = context.exception
        self.assertTrue("database is not open" in the_exception.args)

    def test_12_GetAllFilePathListPathWhenDatabaseOpen(self):
        DatabaseOpen = self.db.open(self.request)
        self.assertTrue(DatabaseOpen)
        ContainsFileTrue = self.db.get_all_Path()
        self.assertEqual(type(ContainsFileTrue), list)

    def test_13_GetAllFilePathThrowsIfDatabaseIsNotOpen(self):
        with self.assertRaises(RuntimeError) as context:
            self.assertTrue(self.db.get_all_Path())
        the_exception = context.exception
        self.assertTrue("database is not open" in the_exception.args)

    def test_14_AddInvalidListPathWhenDatabaseOpen(self):
        DatabaseOpen = self.db.open(self.request)
        self.assertTrue(DatabaseOpen)
        InvalidLink = self.db.add_invalidLink(self.path, self.link)
        self.assertEqual(InvalidLink, str(self.path)+","+str(self.link))

    def test_15_AddInvalidLinkThrowsIfDatabaseIsNotOpen(self):
        with self.assertRaises(RuntimeError) as context:
            self.assertTrue(self.db.add_invalidLink("",""))
        the_exception = context.exception
        self.assertTrue("database is not open" in the_exception.args)

    def test_16_ContainsInvalidLinkWhenDatabaseOpen(self):
        DatabaseOpen = self.db.open(self.request)
        self.assertTrue(DatabaseOpen)
        ContainsFile = self.db.contains_invalidLink(self.path, self.link)
        self.assertIn(ContainsFile, [True, False])

    def test_17_ContainsInvalidLinkThrowsIfDatabaseIsNotOpen(self):
        with self.assertRaises(RuntimeError) as context:
            self.assertTrue(self.db.contains_invalidLink("/path","/link"))
        the_exception = context.exception
        self.assertTrue("database is not open" in the_exception.args)

    def test_18_GetInvalidLinksListWhenDatabaseOpen(self):
        DatabaseOpen = self.db.open(self.request)
        self.assertTrue(DatabaseOpen)
        ContainsInvalidLinks = self.db.get_invalid_links(self.path)
        self.assertEqual(type(ContainsInvalidLinks), list)

    def test_19_GetInvalidLinkThrowsIfDatabaseIsNotOpen(self):
        with self.assertRaises(RuntimeError) as context:
            self.assertTrue(self.db.get_invalid_links("/path"))
        the_exception = context.exception
        self.assertTrue("database is not open" in the_exception.args)

    def test_20_GetAllInvalidLinkSetPathWhenDatabaseOpen(self):
        DatabaseOpen = self.db.open(self.request)
        self.assertTrue(DatabaseOpen)
        ContainsFileTrue = self.db.get_all_invalid_links()
        self.assertEqual(type(ContainsFileTrue), set)

    def test_21_GetAllInvalidLinksThrowsIfDatabaseIsNotOpen(self):
        with self.assertRaises(RuntimeError) as context:
            self.assertTrue(self.db.get_all_invalid_links())
        the_exception = context.exception
        self.assertTrue("database is not open" in the_exception.args)




if __name__ == '__main__':
    unittest.main(verbosity=2)
