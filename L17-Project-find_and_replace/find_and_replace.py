import os
import re


class FindAndReplace:
    def __init__(self, root_path: str):
        self._root_path = root_path

    # list all the files and folder in the path provided
    @staticmethod
    def list(path: str):
        # to return a list of files
        
        return [
            folder + "/" + path
            for folder, subfolders, file_paths in os.walk(path)
            for path in file_paths
        ]

    @staticmethod
    def replace_in_file(file_path, find, replace):
        # r+ for read and writing file
        with open(file_path, 'r+') as file:
            content = file.read()

            replaced = re.sub(find, replace, content)
            # set the cursor to the beginning of the file, otherwise the cursor will be at the end of the file
            file.seek(0)
            # we will truncate, ie remove the existing content of the file before writing the replaced content
            file.truncate()
            # write new content to the file
            file.write(replaced)

    def replace_text(self, find, replace, ignored_extensions: list = []):
        # list all the files and folder in the path provided recursively
        files = self.list(self._root_path)
        # loop through each item
        for file_path in files:
            filename, extension = os.path.splitext(file_path)

            if extension in ignored_extensions:
                continue

            # find content and replace with text
            self.replace_in_file(file_path, find, replace)


if __name__ == '__main__':
    cwd = os.getcwd()

    searcher = FindAndReplace(cwd + "/sample")

    find = input("What to replace? Enter: ")

    replace = input("What to replace with? Enter: ")

    searcher.replace_text(find, replace, ['.py'])

