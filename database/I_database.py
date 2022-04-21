import os
from database import TextFile_database


def FileTable():
    return os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'database',"FileTable.txt"))

def InvalidLinks():
    return os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'database',"InvalidLinks.txt"))


class IDatabase():
    pass

