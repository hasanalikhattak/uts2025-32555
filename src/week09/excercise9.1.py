import json
import csv
from collections import Counter
import os
from typing import Dict

class VowelCounter:
    VOWELS = 'aeiouAEIOU'
    
    def __init__(self):
        self.data_txt = 'data.txt'
        self.data_json = 'data.json'
        self.data_csv = 'data.csv'
        self.ensure_files_exist()

    def ensure_files_exist(self):
        for file in [self.data_txt, self.data_json, self.data_csv]:
            if not os.path.exists(file):
                with open(file, 'w') as f:
                    pass

    def count_vowels(self, text: str) -> Dict[str, int]:
        counter = Counter(char for char in text if char in self.VOWELS)
        return dict(counter)

    def write_to_txt(self, counts: Dict[str, int]):
        with open(self.data_txt, 'a') as f:
            for vowel, freq in counts.items():
                f.write(f"{vowel} --> {freq}\n")

    def write_to_json(self, counts: Dict[str, int]):
        with open(self.data_json, 'r+') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}
            for vowel, freq in counts.items():
                data[vowel] = data.get(vowel, 0) + freq
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()

    def write_to_csv(self, counts: Dict[str, int]):
        with open(self.data_csv, 'a', newline='') as f:
            writer = csv.writer(f)
            for vowel, freq in counts.items():
                writer.writerow([vowel, freq])

    def display_file_contents(self):
        for file in [self.data_txt, self.data_json, self.data_csv]:
            print(f"\nContents of {file}:")
            with open(file, 'r') as f:
                print(f.read())

    def main(self):
        while True:
            user_input = input("Enter a string (or '*' to exit): ")
            if user_input == '*':
                break
            counts = self.count_vowels(user_input)
            self.write_to_txt(counts)
            self.write_to_json(counts)
            self.write_to_csv(counts)
        
        self.display_file_contents()

if __name__ == "__main__":
    vc = VowelCounter()
    vc.main()