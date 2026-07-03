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

    def process_file(self):
        content = self.file_path.exists()
        if content:
            with self.file_path.open() as f:
                lines = f.readlines()
                for line in lines:
                    print(line)

path = WordAnalyzer("random.txt")
path.process_file()
    