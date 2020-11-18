
import pickle
import os


class Data:

    def __init__(self, file):
        self.file = file


    def build(self, data={}):
        self.save(data=data)

    def destroy(self):
        os.remove(self.file)

    def load(self):
        with open(self.file, 'rb') as file:
            return pickle.load(file)

    def save(self, data={}):
        with open(self.file, 'wb') as file:
            pickle.dump(data, file)

    