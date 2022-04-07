import os
from urllib.parse import urlparse
import fnmatch
from modules import I_search_file
from modules import smb_connection

class SmbSearch(I_search_file.FileSearchStrategy):
    def smbwalk(self, conn, shareddevice, top = u'/'):
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
                for x in self.smbwalk(conn, shareddevice, new_path):
                    yield x     
            except:
                pass

    
    def search_file(self, search_path, list_searchstring):
        url_parsed              = urlparse(search_path)
        share_name              = (url_parsed.path.split("/"))[1]
        top                     = (url_parsed.path.split(share_name))[1]
        self.conn               = smb_connection.SmbServerConnectionHandler().get_existing_connection(search_path)
        search_result = []
        for folder in self.smbwalk(self.conn, share_name, top):
            path = folder[0]
            for file in folder[2]:
                file_name = os.path.join(path, file)
                if fnmatch.fnmatch(file_name, list_searchstring):
                    search_result.append(file_name)

        return search_result
