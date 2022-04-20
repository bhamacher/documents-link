from abc import ABC, abstractmethod


class IDatabase(ABC):

    def __init__(self):
        pass

    ## open existing db
    @abstractmethod
    def open_db(file_path):
        # open database
        return True

    ## close existing db
    @abstractmethod
    def close_db(file_path):
        # close database
        return True

    ## contain invalid link
    @abstractmethod
    def contain_invalid_link(file_path):
        # open database
        # check inside database
        return True


    ## add invalidlink
    @abstractmethod
    def add_invalidlink(file_path):
        # if found then add else not
        pass
        

    ## check data with ID
    @abstractmethod
    def id_db(file_path):
        pass


    ## delete data with ID
    @abstractmethod
    def del_id_db(file_path):
        # delete with its ID
        pass

    ## contain file
    @abstractmethod
    def contain_file():
        pass

