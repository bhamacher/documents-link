import unittest
from getpass import getpass
from database import I_database

smb_data = "smb://s-zera-stor01/data1/Zusammenarbeit/Transferordner/EW/DKU"

class Test(unittest.TestCase):


    def test_1_database(self):
        user_name           = getpass(prompt = 'Give your user_name: ')
        password            = getpass(prompt = 'Give your password: ')
        smb_objective       = I_database.IDatabank()
        connection = smb_objective.add_db(smb_data, user_name, password)
        self.assertIsNotNone(connection)

if __name__ == '__main__':
    unittest.main(verbosity=2)