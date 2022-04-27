import getopt
from document_links import local_search
from document_links.database import TextFile_database
import os

from document_links.database.IDatabase import IDatabase



def test_link_data():
    return os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'test_folder','folder_test'))


class DocumentLinks():

    def __init__(self, db : IDatabase):
        self.db = db
        pass

    # find all files on drive and write to filetable form here
    def update_filetable(self,args):
        print("update_filetable called with "+args[0])
        options, remainder = getopt.getopt(args, '', ['help'])
        for opt, arg in options:
            if opt in ('--help'):
                self.__show_update_filetable_help()
                return
            else:
                self.__show_update_filetable_help()
                return
        
        ## local file
        local_file = local_search.LocalFileSearch().search_file(args[0], "*")
        ## database
        self.db.open()
        for file in local_file:
            self.db.add_filePath(file)
        return True


    def clean_filetable(self,args):
        # f = open(FileTable(), "r+")
        # f.truncate(0)
        # f.close()
        return True

    def check_links(self,args):
        print("check_links called")
        pass

    def store_credentials(self,args):
        print("store_crednetials called")
        pass



    def __show_update_filetable_help(self):
        print("document-links update-filetable <path>")


        

# python document-links.py update-filetable