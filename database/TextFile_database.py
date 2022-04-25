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
        f1.close()
        f2.close()
        return True
        
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

    def remove_filePath(self,path):
        ## remove path
        if not self.text_file_database.closed:
            if self.contains_filePath(path) == True:
                with open(self.text_file_database.name) as f:
                    lines = f.readlines()
                    lines.remove(path+"\n")
                    with open(self.text_file_database.name, "w+") as new_f:
                        for line in lines:        
                            new_f.write(line)

        ## remove invalid links assigned to this path
        if not self.invalid_link_database.closed:
            invalid_links = self.get_invalid_links(path)
            i = 0
            len_link = len(invalid_links)
            while i < len_link:
                print("A",invalid_links)
                with open(self.invalid_link_database.name) as f:
                    lines = f.readlines()
                    lines.remove(invalid_links[i] + "\n")
                    with open(self.invalid_link_database.name, "w+") as new_f:
                        for line in lines:        
                            new_f.write(line)
                    if i == len_link:
                        break
                    i +=1
            return path

        else:
            raise RuntimeError("database is not open")

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

    def add_invalidLink(self,path,link):
        path_link = str(path) + "," + str(link)
        if not self.text_file_database.closed:
            if self.contains_filePath(link) == False:
                if not self.invalid_link_database.closed:
                    if self.contains_invalidLink(path,link) == False:
                        self.invalid_link_database.write(path_link + "\n")
                    return path_link
        else:
            raise RuntimeError("database is not open")

    def remove_invalidLink(self,path,link):
        """!
        Remove invalid link from database
        e.g. /s-zera-stor01/..../File1.docx

        contains_invlaidLInk will return false for this link and file combination
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
        if not self.invalid_link_database.closed:
            with open(self.invalid_link_database.name) as f:
                path_link = str(path) + "," + str(link)
                if path_link in str([line.rstrip('\n') for line in f]):
                    return True
                else:
                    return False
        else:
            raise RuntimeError("database is not open")

    def get_invalid_links(self,path):
        if not self.invalid_link_database.closed:
            all_link = []
            with open(self.invalid_link_database.name) as searchfile:
                for line in searchfile:
                    if path in line:
                        all_link.append(line.replace("\n",""))
                return all_link

        else:
            raise RuntimeError("database is not open")

    def get_all_invalid_links(self):
        if not self.invalid_link_database.closed:
            with open(self.invalid_link_database.name) as f:
                data_into_list = f.read().split("\n")
            return set(data_into_list)
        else:
            raise RuntimeError("database is not open")

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