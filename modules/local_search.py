import glob
import os
from modules import I_search_file

class LocalFileSearch(I_search_file.FileSearchStrategy):
    @staticmethod
    def search_file(search_path, list_searchstring):
        search_path = search_path.replace('/', os.path.sep)
        search_path = search_path.replace('\\', os.path.sep)
        if not os.path.isdir(search_path):
            return None
        search_result = []

        for root, dirs, _files in os.walk(search_path):
            for directory in dirs:
                for search_string in list_searchstring:
                    globpath = os.path.join(root, directory, search_string)
                    for filename in glob.glob(globpath):
                        search_result.append(filename)
        return search_result
