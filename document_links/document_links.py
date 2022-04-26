from document_links import smb_connection
import getopt

class DocumentLinks():

    def __init__(self) -> None:
        pass

    # find all files on drive and write to filetable form here

    def __show_update_filetable_help(self):
        print("document-links update-filetable <path>")

    def update_filetable(self,args):
        print("update_filetable called with "+args[0])
        options, remainder = getopt.getopt(args, '', ['help'])
        for opt, arg in options:
            if opt in ('--help'):
                self.__show_update_filetable_help()
        pass

    def clean_filetable(self,args):
        print("clean_filetable called")
        pass

    def check_links(self,args):
        print("check_links called")
        pass

    def store_credentials(self,args):
        print("store_crednetials called")
        pass

