import os
from urllib.parse import urlparse
from modules import smb_connection
import tempfile
from urllib.parse import urlparse
from modules import I_copy_file

class SmbCopyFile(I_copy_file.ICopyFileStrategy):

    def __init__(self):
        self.smbServerConnectionHandler = smb_connection.SmbServerConnectionHandler()
        pass

    def copy_file(self, source, destination, user_name, password):
        if "smb://" in source:
            conn = self.smbServerConnectionHandler.get_connection(source, user_name, password)
            path_parse = urlparse(source)
            share_name = path_parse.path.split("/")[1]
            base_file_path = path_parse.path.split(share_name)[1]
            base_file_name = base_file_path.split("/")[-1]
            destination = tempfile.gettempdir() ## check for correct file.
            tmp_file = os.path.join(destination, base_file_name)
            with open(tmp_file, 'wb') as fp: # retrieve smb file to local.
                conn.retrieveFile(share_name, base_file_path, fp)
            return True

        else:
            return False
