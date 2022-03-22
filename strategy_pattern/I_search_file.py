from abc import ABC, abstractmethod

## Strategy interface
class FileSearchStrategy(ABC):
    @abstractmethod
    def search_file(search_path, list_searchstring):
        pass
    