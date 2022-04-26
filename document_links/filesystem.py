from document_links import I_search_file
from document_links import I_copy_file

## context - the primary class
class FileSystem:

    def __init__(self, searchstrategy: I_search_file.ISearchFileStrategy, copystrategy: I_copy_file.ICopyFileStrategy):
        self.searchstrategy = searchstrategy
        self.copystrategy = copystrategy

    def search_file(self, search_path, list_searchstring):
        return self.searchstrategy.search_file(search_path, list_searchstring)

    def copy_file(self, source, destination, user_name, password):
        return self.copystrategy.copy_file(source, destination, user_name, password)
