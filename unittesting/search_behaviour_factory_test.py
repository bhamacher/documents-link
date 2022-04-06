
import unittest
from modules import SearchBehaviourFactory
from modules import smb_search
from modules import local_search

class Test(unittest.TestCase):

    def test_create_smb_connection(self):
        path_name = "smb://s-zera-stor01/data1/Zusammenarbeit/Transferordner/EW/DKU/test_link_data/docx_data/Abt-TB-2021-05-03.docx"
        factory = SearchBehaviourFactory.SearchBehaviourFactory()
        behaviour=factory.CreateSearchBehaviour(path_name)
        self.assertTrue(isinstance(behaviour,smb_search.SmbSearch))
        self.assertFalse(isinstance(behaviour,local_search.LocalFileSearch))
        pass

    def test_create_local_connection(self):
        path_name = r'M:\data1\Zusammenarbeit\Transferordner\EW\DKU\test_link_data\docx_data\Abt-TB-2021-05-03.docx'
        factory = SearchBehaviourFactory.SearchBehaviourFactory()
        behaviour=factory.CreateSearchBehaviour(path_name)
        # TODO: This will fail: Factory must implement behaviour.
        self.assertTrue(isinstance(behaviour,local_search.LocalFileSearch))
        self.assertFalse(isinstance(behaviour,smb_search.SmbSearch))
        pass



if __name__ == '__main__':
    unittest.main(verbosity=2)