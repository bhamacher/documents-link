import unittest
import os
from database import TextFile_database


def FileTable():
    return os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'database',"FileTable.txt"))

def InvalidLinks():
    return os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'database',"InvalidLinks.txt"))



class Test(unittest.TestCase):

    def test_OpenDatabase(self):
        request=TextFile_database.databaseOpenRequest()
        db=TextFile_database.TextFileDatabase()
        self.assertTrue(db.open(request))
    
    def test_OpenDatabaseWithWrongTypeThrowsException(self):
        with self.assertRaises(ValueError) as context:
            request="/file/path/file.txt"
            db=TextFile_database.TextFileDatabase()
            self.assertTrue(db.open(request))
        the_exception=context.exception
        self.assertTrue("Invalid database type" in the_exception.args)
    
    def test_IsOpenReturnsFalse(self):
        pass

    def test_IsOpenReturnsTrueWhenDatabaseOpenWasCalled(self):
        pass

    def test_CloseDatabase(self):
        pass

    def test_IsOpenReturnsFalseWhenDatabaseOpenAndCloseWasCalled(self):
        pass
    
    def test_AddFilePathThrowsIfDatabaseIsNotOpen(self):
        with self.assertRaises(RuntimeError) as context:
            request="/file/path/file.txt"
            db=TextFile_database.TextFileDatabase()
            self.assertTrue(db.add_filePath("path"))
        the_exception=context.exception
        self.assertTrue("database is not open" in the_exception.args)

if __name__ == '__main__':
    unittest.main(verbosity=2)
