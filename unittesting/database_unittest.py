import unittest
import os
from database import TextFile_database


def FileTable():
    return os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'database',"FileTable.txt"))

def InvalidLinks():
    return os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'database',"InvalidLinks.txt"))



class Test(unittest.TestCase):

    def test_1(self):
        objective               = TextFile_database.TextFileDatabase()
        file_open_object1           = objective.open(FileTable(), InvalidLinks())
        file_isOpen_object1         = objective.isOpen()
        file_close_object1          = objective.close()

        file_open_object2           = objective.open(InvalidLinks(), InvalidLinks())
        file_isOpen_object2         = objective.isOpen()
        file_close_object2          = objective.close()

        self.assertTrue(file_open_object1)
        self.assertTrue(file_isOpen_object1)
        self.assertTrue(file_close_object1)

        self.assertTrue(file_open_object2)
        self.assertTrue(file_isOpen_object2)
        self.assertTrue(file_close_object2)

if __name__ == '__main__':
    unittest.main(verbosity=2)
