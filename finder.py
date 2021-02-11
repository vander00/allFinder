import os
import textract
from fuzzywuzzy import fuzz


class Finder:
    # --- Data ---
    FILES_NAMES = [["txt", 'log', 'html', 'css', 'cpp', 'h', 'js', 'py', 'c'], ['doc', 'docx', 'rtf', 'odt']]  # Supported file formats

    def __init__(self):
            self.feeling = True  # Check if text is found

    def checker_default(self, catalog_name, find_str, name_file):
        # ---Data---
        numbers_str = list()  # Lines with text
        number_str = 1  # The line where the text was found
        numbers_repeat = 0  # Repeating text in a file

        with open(catalog_name + "/" + name_file, 'r', encoding='utf-8') as f:  # Opening a file
            for line in f:
                if fuzz.partial_ratio(find_str, line) > 88:  # If the lines match more than 89, then the information is displayed
                    self.feeling = False
                    numbers_repeat += 1
                    numbers_str.append(number_str)
                    number_str = 0
                number_str += 1
            if numbers_repeat != 0:
                print(f"\nPath to the file: {catalog_name + '/' + name_file}.")
                print(f'Content lines: {str(numbers_str).replace(",", " |")}')
                print(f"String repetitions: {numbers_repeat}")

    def checker_other(self, catalog_name, find_str, name_file):  # Checking files from the FILES_NAMES list
        if find_str in textract.process(catalog_name + "/" + name_file).decode('utf-8').lower():
            self.feeling = False
            print(f"Path to the file: {catalog_name + '/' + name_file}")

    def run(self):  # Main function
        while True:
            catalog_name = input("Directory path (C:/program): ")
            find_str = input("\nText to find: ").lower()

            try:
                catalog = os.listdir(catalog_name)
                for name in catalog:
                    if name.split('.')[-1] in Finder.FILES_NAMES[0]:
                        self.checker_default(catalog_name, find_str, name)
                    elif name.split('.')[-1] in Finder.FILES_NAMES[1]:
                        self.checker_other(catalog_name, find_str, name)
                if self.feeling == True:
                    print("The text was not found. ;(")
            except FileNotFoundError:
                print('\nError! You entered an invalid file path.')
            self.feeling = True


if __name__ == "__main__":
    program = Finder()
    program.run()
