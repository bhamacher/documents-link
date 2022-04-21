from os.path import exists
from database import IDatabase
import io
import os


def FileTable():
    return os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'database',"FileTable.txt"))

def InvalidLinks():
    return os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'database',"InvalidLinks.txt"))


class databaseOpenRequest:
    text_file_database : str
    invalid_link_database : str


class TextFileDatabase(IDatabase.IDatabase):

    def __init__(self):
        super().__init__()
        self.text_file_database = io.StringIO("")
        self.invalid_link_database = io.StringIO("")
        self.invalid_link_database.close()
        self.text_file_database.close()
    
    def open(self,database : databaseOpenRequest):
        if type(database) is not databaseOpenRequest:
            raise ValueError("Invalid database type")

        self.text_file_database = FileTable()
        self.invalid_link_database = InvalidLinks()

        # check whether given database exit or not.
        if exists(self.text_file_database):
            self.text_file_database = open(self.text_file_database, "a+")
        else:
            open(self.text_file_database, "w+")

        if exists(self.invalid_link_database):
            self.invalid_link_database = open(self.invalid_link_database, "a+")
        else:
            open(self.invalid_link_database, "w+")

        return True

   
    def close(self):
        f1 = self.text_file_database
        f2 = self.invalid_link_database
        try:
            f1.close()
            f2.close()
            return True
        except:
            return False
   
    def isOpen(self):
        if not self.text_file_database.closed or not self.invalid_link_database.closed:
            return True

        else:
            return False
        
    def add_filePath(self,path):
        if not self.text_file_database.closed:
            if self.contains_filePath(path) == False:
                self.text_file_database.write(path + "\n")
            return path
        else:
            raise RuntimeError("database is not open")


    def remove_filePath(self,path): ## and truncate
        if not self.text_file_database.closed:
            pass
        else:
            raise RuntimeError("database is not open")



        """!
        Remove file path from database
        e.g. /s-zera-stor01/..../File1.docx

        contains_filePath will return false for this path and
        get_all_path will not list this path further.

        Furthermore all invlaid links assigned to this file will be deleted as well.

        @Param path  The absolute filepath

        @return unique id to indentify file path. Can be file path

        @throw RuntimeError if database is not open
        """


    def contains_filePath(self,path):
        if not self.text_file_database.closed:
            with open(self.text_file_database.name) as f:
                if path in str([line.rstrip('\n') for line in f]):
                    return True
                else:
                    return False
        else:
            raise RuntimeError("database is not open")


    def get_all_Path(self):
        if not self.text_file_database.closed:
            with open(self.text_file_database.name) as f:
                data_into_list = f.read().split("\n")
            return data_into_list
        else:
            raise RuntimeError("database is not open")

        """!
        Return list with all stored path

        @return list() with all path

        @throw RuntimeError if database is not open
        """


    def add_invalidLink(self,path,link):

        """!
        Add invalid link to database
        The link is assigned to the file where it was found in.

        @param path  file that contains invlaid link
        @param link  the invalid link itself

        @return unique id to indentify link path. Can be link itself   

        @throw RuntimeError if database is not open    
        """
        pass


    def remove_invalidLink(self,path,link):
        """!
        Remove invalid link from database
        e.g. /s-zera-stor01/..../File1.docx

        contains_invlaidLInkwill return false for this link and file combination
        get_invalid_links will not list this further for this path.

        Furthermore all invlaid links assigned to this file will be deleted as well.

        @Param path  The file the contained the invlaid link
        e.g. /s-zera-stor01/..../File1.docx
        @Param link  The once invlaid link itself
        e.g. /s-zera-stor01/..../File2.docx

        @return unique id to indentify link path. Can be link itself
        e.g /s-zera-stor01/..../File2.docx

        @throw RuntimeError if database is not open
        """
        pass


    def contains_invalidLink(self,path,link):
        """!
        Return true if invalid link is stored for path in db

        @param path  The file that conatains the invalid link
        e.g. /s-zera-stor01/..../File1.docx

        @param link  The invalid link itself
        e.g /s-zera-stor01/..../File2.docx


        @return true if file (param path) has invalid link (param link) otherwise false

        @throw RuntimeError if database is not open
        """
        pass


    def get_invalid_links(self,path):
        """!
        Return list with all invalid links stored for file path

        @param path  path toi file that conatins invalid links

        @return list() with invlaid links contained in path

        @throw RuntimeError if database is not open
        """
        pass


    def get_all_invalid_links(self):
        """!
        Returns set with all invalid links found independet from file path 

        @return set() with all invalid links

        @throw RuntimeError if database is not open
        """
        pass


    def remove_all_occurence_of_invalid_link(self,link):
        """!
        Removes all occurences of an invlaid link from database

        Neither get_invalid_links nor get_all_invalid_links will return 
        this link after this function call

        @param the link to remove from the entire database
        e.g /s-zera-stor01/..../File2.docx
        
        @returns unique id of link. Can be link itself

        @throw RuntimeError if database is not open
        """
        pass