from smb.SMBConnection import SMBConnection
from getpass import getpass
import os
import socket

class SmbConnection:
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
                for x in smbwalk(conn, shareddevice, new_path):
                    yield x     
            except:
                pass

    
    password = getpass(prompt='Input your password: ')
    share_name          = "data1"
    user_name           = "d.kumar"         
    local_machine_name  = "kumar"    
    server_machine_name = "s-zera-stor01"
    server_IP           =  socket.gethostbyname(server_machine_name)
    print(server_IP)
    conn = SMBConnection(user_name, password, local_machine_name, server_machine_name, use_ntlm_v2 = True)
    assert conn.connect(server_IP, 139)
    top_object =  '/'
    ans = smbwalk(conn, share_name,top = top_object)
        







