import unittest
from document_links import FileSystemBehaviourFactory
from document_links import smb_search
from document_links import local_search
from document_links import local_copy_file
from document_links import smb_copy_file


class Test(unittest.TestCase):

    def test_create_smb_connection(self):
        path_name = "smb://s-zera-stor01/data1"
        behaviour = FileSystemBehaviourFactory.CreateSearchBehaviour(path_name)
        self.assertIsInstance(behaviour,smb_search.SmbSearch)
        self.assertNotIsInstance(behaviour,local_search.LocalFileSearch)

    def test_create_local_connection(self):
        path_name = "\\s-zera-stor01\data1\Zusammenarbeit"
        behaviour = FileSystemBehaviourFactory.CreateSearchBehaviour(path_name)
        self.assertIsInstance(behaviour,local_search.LocalFileSearch)
        self.assertNotIsInstance(behaviour,smb_search.SmbSearch)

    def test_create_smb_copy(self):
        path_name = "smb://s-zera-stor01/data1"
        behaviour = FileSystemBehaviourFactory.CreateCopyBehaviour(path_name)
        self.assertIsInstance(behaviour,smb_copy_file.SmbCopyFile)
        self.assertNotIsInstance(behaviour,local_copy_file.LocalCopyFile)


    def test_create_local_copy(self):
        path_name = "\\s-zera-stor01\data1\Zusammenarbeit"
        behaviour = FileSystemBehaviourFactory.CreateCopyBehaviour(path_name)
        self.assertIsInstance(behaviour,local_copy_file.LocalCopyFile)
        self.assertNotIsInstance(behaviour,smb_copy_file.SmbCopyFile)



if __name__ == '__main__':
    unittest.main(verbosity=2)
