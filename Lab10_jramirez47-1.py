"""
Word Counter
Johan D. Ramirez Maldonado
Counts words
Uses 4 predefined files provided by the instructor
07/02/2026
"""
from pathlib import Path
import json

class WordAnalyzer:
    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.__dict = {}

    def process_file(self):
        content = self.file_path.exists()
        try:
            if not content:
                raise FileNotFoundError
        except FileNotFoundError:
            print(f"The file {self.file_path} wasn't found.")
        empty_dict = {}
        punc_tuple = (".", ",", "!", "?", ";", ":", "-", "_", "'", '"', "(", ")", "[", "]", "{", "}", "/", "\\")
        if content:
            with self.file_path.open() as f:
                lines = f.readlines()
                for line in lines:
                    for punc in punc_tuple:
                        if punc == "-" or punc == "_":
                            line = line.replace(punc, " ")
                        else:
                            line = line.replace(punc, "")
                    line = line.lower()
                    line = line.split()
                    for word in line:
                        if word in empty_dict:
                            empty_dict[word] += 1
                        else:
                            empty_dict[word] = 1
            self.__dict = empty_dict
            return True
        else:
            return False

    def print_report(self):
        sorted_dict = sorted(self.__dict.keys())
        for key in sorted_dict:
            print(f"{key} :: {self.__dict[key]}")


path = WordAnalyzer("random.txt")
path.process_file()
path.print_report()
    