import I_search_file

## context - the primary class
class FileSearch:
    strategy: I_search_file.FileSearchStrategy  ## the strategy interface

    def __init__(self, strategy: I_search_file.FileSearchStrategy):
        self.strategy = strategy

    def search_file_strategy(self, search_path, list_searchstring):
        return self.strategy.search_file(search_path, list_searchstring)
