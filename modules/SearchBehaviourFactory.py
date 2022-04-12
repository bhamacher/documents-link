from modules import smb_search
from modules import local_search
from modules import local_copy_file
from modules import smb_copy_file




class SearchBehaviourFactory:
    def __init__(self):
         pass

    def CreateSearchBehaviour(self, path):
        self.path = path
        if "smb://" in path:
            return smb_search.SmbSearch()
        else:
            return local_search.LocalFileSearch()

    def CreateCopyBehaviour(self, path):
        self.path = path
        if "smb://" in path:
            return smb_copy_file.SmbCopyFile()
        else:
            return local_copy_file.LocalCopyFile()
