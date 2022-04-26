import os
import os.path

class FilePathValidation:
    @staticmethod
    def path_valid_file(archive_file, destination_path):
        if not os.path.isfile(archive_file):
            return False

        if not os.path.isdir(destination_path):
            return False
        return True
