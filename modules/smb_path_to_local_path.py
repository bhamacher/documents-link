from smb.SMBConnection import SMBConnection
import os
from urllib.parse import urlparse
import smb_connection
import tempfile
from urllib.parse import urlparse


class FileToLocal():

    def __init__(self):
        self.smbServerConnectionHandler = smb_connection.SmbServerConnectionHandler()

    def path_to_local(self, smb_data_path):
        if "smb:" in smb_data_path:
            conn = self.smbServerConnectionHandler.get_connection(smb_data_path)
            path_parse = urlparse(smb_data_path)
            share_name = path_parse.path.split("/")[1]
            base_file_path = path_parse.path.split(share_name)[1]
            base_file_name = base_file_path.split("/")[-1]
            temp_path = tempfile.gettempdir()
            tmp_file = os.path.join(temp_path, base_file_name)
            with open(tmp_file, 'wb') as fp: # retrieve smb file to local.
                conn.retrieveFile(share_name, base_file_path, fp)

            return True

        else:
            return False
