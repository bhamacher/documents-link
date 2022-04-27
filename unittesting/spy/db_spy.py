from document_links.database.IDatabase import IDatabase

class db_spy(IDatabase):

    def __init__(self) -> None:
        self.fileTable=set()
        self.clean_filetable_was_called=False
        super().__init__()

    def open(self):
        pass

    def close(self):
        pass

    def isOpen(self):
        pass


    def add_filePath(self,path):
        self.fileTable.add(path)
        return path
    
    def remove_filePath(self,path):
        pass

    def contains_filePath(self,path):
        pass

    def get_all_Path(self):
        pass

    def add_invalidLink(self,path,link):
        pass

    def remove_invalidLink(self,path,link):
        pass


    def contains_invalidLink(self,path,link):
        pass

    def get_invalid_links(self,path):
        pass


    def get_all_invalid_links(self):
        pass

    def remove_all_occurence_of_invalid_link(self,link):
        pass
