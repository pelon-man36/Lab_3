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
        try:
            self.file_path.exists()
        except FileNotFoundError:
            print(f"File not found")
    