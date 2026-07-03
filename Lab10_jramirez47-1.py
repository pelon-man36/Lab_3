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
        punc_tuple = (".", ",", "!", "?", ";", ":", "-", "_", "'", '"', "(", ")", "[", "]", "{", "}", "/", "\\", "—", "‘", "†", "•", '”', '“', "’")
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
        print()

def main():
    files = {1: "monte_cristo.txt", 2: "princess_mars.txt", 3: "Tarzan.txt", 4: "treasure_island.txt"}
    clean_files = {1: "Monte Cristo", 2: "Princess Mars", 3: "Tarzan", 4: "Treasure Island"}
    opt_out = True
    opt_cont = True

    while opt_cont:
        opt_again = True
        print("-- Word Analyzer --")
        print("Select a file to analyze:\n")
        for key in clean_files:
            print(f"{key}. {clean_files[key]}")
        print("5. Exit")

        while opt_out:
            try:
                option = int(input("Select a file to analyze (1-5): "))
                if option <= 0 or option >= 6:
                    raise KeyError
            except ValueError, KeyError:
                print("Invalid option.\n")
                continue
            else:
                if option == 5:
                    opt_out = False
                    opt_cont = False
                    opt_again = False
                else:
                    print(f"Processing file: {files[option]}\n")
                    print(files[option])
                    opt_out = False
                    path = WordAnalyzer(files[option])
                    path.process_file()
                    path.print_report()

        while opt_again:
            try:
                option = input("Would you like to analyze another file? (y/n): ")
                if option.lower() == "n":
                    opt_again = False
                    opt_cont = False
                elif option.lower() == "y":
                    opt_again = False
                    opt_out = True
                else:
                    raise ValueError
            except ValueError:
                print("Invalid option.\n")
    print("Thank you. Goodbye.")
            


#path = WordAnalyzer("random.txt")
#path.process_file()
#path.print_report()

if __name__ == "__main__":
    main()