
from abc import ABC, abstractmethod

class IDatabase(ABC):

    """!
    Database interfasce class

    Defines database behaviour. The database caches data found on the shared drives.
    The cached data are the files found and the invalid links found inside these files.

    For each implementation of this interface unittests should be created.
    Please make sure to test all exceptions too.
    """


    @abstractmethod
    def open(self):
        """!
        Opens existing database or creates new one if db does not exist

        @param database  Database connection information
        For example filePath for txt or json file implementation

        @return true if succeeds

        @throws IllegalArgumentException
        The database object can be of different types depending on the used database
        implementation. If the databaseparameter does not provide the needed information 
        the exception will be thrown
        """
        pass

    @abstractmethod
    def close(self):
        """!
        Close open database

        @return true if database was open false otherwise
        """
        pass
    
    @abstractmethod
    def isOpen(self):
        """!
        Returns status of database

        @return true if open false otherwise
        """
        pass

    @abstractmethod
    def add_filePath(self,path):
        """!
        Adds file path to database
        e.g. /s-zera-stor01/..../File1.docx

        @Param path  The absolute filepath

        @return unique id to indentify file path. Can be file path

        @throw RuntimeError if database is not open
        """
        pass
    
    @abstractmethod
    def remove_filePath(self,path):
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
        pass

    @abstractmethod 
    def contains_filePath(self,path):
        """!
        Return true if path is stored in database

        @param path  The expected path 

        @return true if path was found false othwerwise

        @throw RuntimeError if database is not open
        """
        pass
    
    @abstractmethod
    def get_all_Path(self):
        """!
        Return list with all stored path

        @return list() with all path

        @throw RuntimeError if database is not open
        """
        pass

    @abstractmethod
    def add_invalidLink(self,path,link):
        """!
        Add invalid link to database
        The link is assigned to the file where it was foiund in.

        @param path  file that contains invlaid link
        @param link  the invalid link itself

        @return unique id to indentify link path. Can be link itself   

        @throw RuntimeError if database is not open    
        """
        pass

    @abstractmethod
    def remove_invalidLink(self,path,link):
        """!
        Remove invalid link from database
        e.g. /s-zera-stor01/..../File1.docx

        contains_invlaidLink will return false for this link and file combination
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

    @abstractmethod
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

    @abstractmethod
    def get_invalid_links(self,path):
        """!
        Return list with all invalid links stored for file path

        @param path  path toi file that conatins invalid links

        @return list() with invlaid links contained in path

        @throw RuntimeError if database is not open
        """
        pass

    @abstractmethod
    def get_all_invalid_links(self):
        """!
        Returns set with all invalid links found independet from file path 

        @return set() with all invalid links

        @throw RuntimeError if database is not open
        """
        pass

    @abstractmethod
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