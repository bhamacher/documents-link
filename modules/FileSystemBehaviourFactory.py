from modules import smb_search
from modules import local_search
from modules import local_copy_file
from modules import smb_copy_file


def CreateSearchBehaviour(path):
    if "smb://" in path:
        return smb_search.SmbSearch()
    else:
        return local_search.LocalFileSearch()

def CreateCopyBehaviour(path):
    if "smb://" in path:
        return smb_copy_file.SmbCopyFile()
    else:
        return local_copy_file.LocalCopyFile()