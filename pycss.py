
import os

class PyCss:

    def load(self, path):
        try:
            with open(path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            raise Exception(f"'{path}' file not found !")