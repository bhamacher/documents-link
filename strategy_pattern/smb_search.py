from smb.SMBConnection import SMBConnection
from getpass import getpass
import os
import socket
from urllib.parse import urlparse
import fnmatch
import I_search_file

user_name = getpass(prompt='Input your user_name: ')
password  = getpass(prompt='Input your password: ')

class SmbSearch(I_search_file.FileSearchStrategy):
    @staticmethod
    def smbwalk(conn, shareddevice, top = u'/'):
        dirs , nondirs = [], []
        names = conn.listPath(shareddevice, top)
        for name in names:
            if name.isDirectory:
                if name.filename not in [u'.', u'..']:
                    dirs.append(name.filename)    
            else:
                nondirs.append(name.filename)
        yield top, dirs, nondirs
        for name in dirs:
            try:
                new_path = os.path.join(top, name)
                for x in SmbSearch.smbwalk(conn, shareddevice, new_path):
                    yield x     
            except:
                pass

    @staticmethod
    def search_file(search_path, list_searchstring):
        url_parsed              = urlparse(search_path)
        server_IP               = socket.gethostbyname(url_parsed.netloc)
        server_machine_name     = url_parsed.netloc
        share_name              = (url_parsed.path.split("/"))[1]
        top                     = (url_parsed.path.split(share_name))[1]
        conn                    = SMBConnection(user_name, password, "", server_machine_name, use_ntlm_v2 = True)
        assert conn.connect(server_IP, 139)

        search_result = []
        for folder in SmbSearch.smbwalk(conn, share_name, top):
            path = folder[0]
            for file in folder[2]:
                file_name = os.path.join(path, file)
                if fnmatch.fnmatch(file_name, list_searchstring):
                    search_result.append(file_name)

        return search_result
