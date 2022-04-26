from abc import ABC, abstractmethod

## Strategy interface
class ISearchFileStrategy(ABC):
    @abstractmethod
    def search_file(self,search_path, list_searchstring):
        pass
