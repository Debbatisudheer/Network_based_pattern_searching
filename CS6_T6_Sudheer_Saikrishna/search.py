import re

class Search:
    def __init__(self, filename="default.txt"):
        self.filename = filename
        try:
            with open(self.filename, 'r') as file:
                self.lines = file.readlines()
        except FileNotFoundError:
            raise Exception(f"File '{self.filename}' not found.")

    def clean(self):
        self.lines = [re.sub(r'[^\w\s]', '', line) for line in self.lines]

    def getLines(self, word):
        result = [word]
        for idx, line in enumerate(self.lines, 1):
            if word in line:
                result.append((idx, line.strip()))
        return result