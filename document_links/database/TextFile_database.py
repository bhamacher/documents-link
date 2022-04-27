from os.path import exists
from document_links.database import IDatabase
import io

class databaseProperties:
    text_file_database_name : str
    invalid_link_database_name : str

class TextFileDatabase(IDatabase.IDatabase):

    def __init__(self, databaseProp : databaseProperties):
        if type(databaseProp) is not databaseProperties:
            raise ValueError("Invalid database type")
        
        self.databaseProp=databaseProp
        super().__init__()
        self.text_file_database = io.StringIO("")
        self.invalid_link_database = io.StringIO("")
        self.invalid_link_database.close()
        self.text_file_database.close()
    
    def open(self):
        self.text_file_database = open(self.databaseProp.text_file_database_name, "r+")
        self.invalid_link_database = open(self.databaseProp.invalid_link_database_name, "r+")
        self.__reinit_file_access()
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
        self.__throw_if_database_is_closed()
        if self.contains_filePath(path) == False:
            self.text_file_database.write(path + "\n")
        return path

    def remove_filePath(self,path):
        ##remove path
        self.__throw_if_database_is_closed()
        self.__reinit_file_access()
        if self.contains_filePath(path) == True:
            self.text_file_database.seek(0)
            lines = self.text_file_database.readlines()
            lines.remove(path + "\n")
            self.__reinit_file_access()
            self.text_file_database.truncate()
            for line in lines:        
                self.text_file_database.write(line)

        ## remove invalid links assigned to this path
        self.__reinit_file_access()
        invalid_links = list(self.get_invalid_links(path))
        i = 0
        len_link = len(invalid_links)
        while i < len_link:
            self.invalid_link_database.seek(0)
            lines = self.invalid_link_database.readlines()
            lines.remove(path + "," + invalid_links[i] + "\n")
            self.__reinit_file_access()
            self.invalid_link_database.truncate()
            for line in lines:        
                self.invalid_link_database.write(line)
            if i == len_link:
                break
            i +=1
        return path

    def contains_filePath(self,path):
        self.__throw_if_database_is_closed()
        lines = self.text_file_database.readlines()
        for line in lines:
            if line == path + "\n":
                return True
        else:
            return False

    def get_all_Path(self):
        self.__throw_if_database_is_closed()
        self.__reinit_file_access()
        lines=self.text_file_database.readlines()
        return self.__remove_line_breaks(lines)

    def add_invalidLink(self,path,link):
        path_link = str(path) + "," + str(link)
        self.__throw_if_database_is_closed()
        if self.contains_filePath(link) == False:
            if not self.invalid_link_database.closed:
                if self.contains_invalidLink(path,link) == False:
                    self.invalid_link_database.write(path_link + "\n")
        return link

    def remove_invalidLink(self,path,link):
        ## remove invalid list
        self.__throw_if_database_is_closed()
        self.__reinit_file_access()
        path_link = str(path) + "," + str(link)
        if self.contains_invalidLink(path, link) == True:
            self.invalid_link_database.seek(0)
            lines = self.invalid_link_database.readlines()
            lines.remove(path_link + "\n")
            self.__reinit_file_access()
            self.invalid_link_database.truncate()
            for line in lines:        
                self.invalid_link_database.write(line)

        ## remove path, which assigned to invalid list.
        self.__throw_if_database_is_closed()
        self.__reinit_file_access()
        if self.contains_filePath(path) == True:
            self.text_file_database.seek(0)
            lines = self.text_file_database.readlines()
            lines.remove(path + "\n")
            self.__reinit_file_access()
            self.text_file_database.truncate()
            for line in lines:
                self.text_file_database.write(line)
        return link

    def contains_invalidLink(self,path,link):
        self.__throw_if_database_is_closed()
        self.__reinit_file_access()
        path_link = str(path) + "," + str(link)
        if path_link in str([line.rstrip('\n') for line in self.invalid_link_database]):
            return True
        else:
            return False

    def get_invalid_links(self,path):
        self.__throw_if_database_is_closed()
        all_link = []
        self.__reinit_file_access()
        for line in self.invalid_link_database:
            if path in line:
                all_link.append(line)
        return set(self.__extract_invalid_links(self.__remove_line_breaks(all_link)))

    def get_all_invalid_links(self):
        self.__throw_if_database_is_closed()
        self.__reinit_file_access()
        lines = self.invalid_link_database.readlines()
        return set(self.__extract_invalid_links(self.__remove_line_breaks(lines)))
    
    def remove_all_occurence_of_invalid_link(self,link):
        self.__throw_if_database_is_closed()
        self.__reinit_file_access()
        all_invalid_link = []
        for line in self.invalid_link_database:
            if link in line:
                all_invalid_link.append(line)
        i = 0
        len_invalid_link = len(all_invalid_link)
        while i < len_invalid_link:
            self.invalid_link_database.seek(0)
            lines = self.invalid_link_database.readlines()
            lines.remove(all_invalid_link[i])
            self.__reinit_file_access()
            self.invalid_link_database.truncate()
            for line in lines:        
                self.invalid_link_database.write(line)
            if i == len_invalid_link:
                break
            i +=1
        return link
        

### private functions.
    def __remove_line_breaks(self,entries):
        result=[]
        for entry in entries:
            result.append(entry.rstrip('\n'))
        return result

    def __reinit_file_access(self):
        self.text_file_database.seek(0)
        self.invalid_link_database.seek(0)

    def __throw_if_database_is_closed(self):
        if self.isOpen() == False:
            raise RuntimeError("database is not open")

    def __extract_invalid_links(self,entries):
        result=[]
        try:
            for entry in entries:
                result.append(entry.split(r',')[1])
        except:
            reuslt=list()
        return result
