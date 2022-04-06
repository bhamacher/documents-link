from modules import smb_search

class SearchBehaviourFactory:
    # def __init__():
    #     pass


    def CreateSearchBehaviour(self, path):
        return smb_search.SmbSearch()