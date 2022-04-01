from smb.SMBConnection import SMBConnection
import socket
from getpass import getpass

class Singleton_smb_connection(type): # metaclass
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton_smb_connection, cls).__call__(*args, **kwargs)
        else:
            cls._instances[cls].__init__(*args, **kwargs)
        return cls._instances[cls]


class SmbServerConnection(metaclass=Singleton_smb_connection):
    def __init__(self): # Initializing
        self.dict_conn = {}

    def get_connection(self, server_name):
        if not server_name in self.dict_conn:
            user_name           = getpass(prompt='Give your user_name: ')
            password            = getpass(prompt='Give your password: ')
            server_IP           = socket.gethostbyname(server_name)
            server_machine_name = server_name
            conn                = SMBConnection(user_name, password, "", server_machine_name)
            assert conn.connect(server_IP, 139)
            self.dict_conn[server_machine_name] = conn
        return self.dict_conn

    def get_connection_count(self):
        return len(self.dict_conn)

    def __del__(self): # Calling destructor
        self.dict_conn.clear()
