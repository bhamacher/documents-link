import glob
import os

class FileSearch:
    @staticmethod
    def search_file(search_path, list_searchstring):
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
