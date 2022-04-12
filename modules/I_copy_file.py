from abc import ABC, abstractmethod

## Strategy interface
class ICopyFileStrategy(ABC):
    @abstractmethod
    def copy_file(self, source, destination, user_name, password):
        pass
