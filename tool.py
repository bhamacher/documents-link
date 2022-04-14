from getpass import getpass
from modules import smb_copy_file

data_full_path = input("give data full path" + "\n" + "Example for smb : smb://s-zera-stor01/data1/dir/file.docx" + "\n")

if "smb://" in data_full_path:
    user_name           = getpass(prompt = 'Give your user_name: ')
    password            = getpass(prompt = 'Give your password: ')
    destination         = ""
    file_path_object = smb_copy_file.SmbCopyFile()
    search_result = file_path_object.copy_file(data_full_path, destination, user_name, password)
    print(search_result)
    pass
