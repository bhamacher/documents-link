import tempfile
import shutil
from modules import I_copy_file

class LocalCopyFile(I_copy_file.ICopyFileStrategy):

    def copy_file(self, source, destination, user_name, password):
        if not "smb://" in source:
            destination = tempfile.gettempdir()
            shutil.copy(source, destination)
            return True
        else:
            return False
