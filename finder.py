import os
import textract
from fuzzywuzzy import fuzz
from os import system
from colorama import Fore


class Finder:
    # --- Data ---
    DEFAULT_NAMES_FILES = ["txt", 'log', 'html', 'css', 'cpp', 'h', 'js', 'py', 'c']  # Supported file formats
    OTHER_NAMES_FILES = ['doc', 'docx', 'rtf', 'odt']

    def __init__(self):
            self.feeling = True  # Check if text is found
            self.settings_files = {
                'txt': True,
                'log': True,
                'html': True,
                'css': True,
                'cpp': True,
                'h': True,
                'py': True,
                'c': True,
                'doc': True,
                'docx': True,
                'rtf': True,
                'odt': True
            }

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
        try:  # File validation check
            if find_str in textract.process(catalog_name + "/" + name_file).decode('utf-8').lower():
                self.feeling = False
                print(f"Path to the file: {catalog_name + '/' + name_file}")
        except KeyError:
            pass
        except Exception:
            pass

    def settings(self):  # Configuring which extensions are used
        for exp in self.settings_files:  # Output to the configuration console.
            if self.settings_files[exp]:
                print("\t{0:9} | ON".format(Fore.GREEN + exp))
            else:
                print("\t{0:9} | OFF".format(Fore.RED + exp))

        print(Fore.WHITE)

        while True:  # Change configuration
            act = input('\tEnter "back" or "quit" to quit\nThe extension to be turned off / on: ').lower()

            if act in self.settings_files:
                if self.settings_files[act]:
                    self.settings_files[act] = False
                else:
                    self.settings_files[act] = True
                return
            elif act == "back" or act == "quit":
                return
            else:
                print(Fore.RED + '\nError! You entered the wrong file extension\n' + Fore.WHITE)

    def directory(self):  # To find out the directory
        while True:
                    catalog_name = input('Enter "back" to exit\n\tDirectory path (C:/program): ').lower()

                    if catalog_name == "back" or catalog_name == "quit":
                        return
                    elif not os.path.exists(catalog_name):
                        print(Fore.RED + '\nError! You entered an invalid file path.\n' + Fore.WHITE)
                        continue
                    find_str = input("\nText to find: ").lower()

                    catalog = os.listdir(catalog_name)
                    for name in catalog:
                        if name.split('.')[-1] in Finder.DEFAULT_NAMES_FILES:
                            if self.settings_files[name.split('.')[-1]]:
                                self.checker_default(catalog_name, find_str, name)
                        elif name.split('.')[-1] in Finder.OTHER_NAMES_FILES:
                            if self.settings_files[name.split('.')[-1]]:
                                self.checker_other(catalog_name, find_str, name)
                    if self.feeling:
                        print("\nThe text was not found. ;(\n")
                    self.feeling = True

    def run(self):  # Main function
        print('Press CTRL + C to quit.\n')

        while True:
            print("\nTo enter:\n[1] - Start")
            print("[2] - Setting File extensions")

            inlet = input("Enter: ").lower()

            if inlet == "1":
                self.directory()
            elif inlet == "2":
                self.settings()
            else:
                print(Fore.RED + "Error! You entered the wrong command." + Fore.WHITE)


if __name__ == "__main__":  # Start!
    program = Finder()
    program.run()
