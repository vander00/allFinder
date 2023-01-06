import sys
sys.path.insert(1, "../Bin")

import allFinder
from colorama import Fore  # pip install colorama


class Main:
    def __init__(self):
        self.settings_files = allFinder.DefaultSettings.DEFAULT_SETTINGS_FILES

    def settings(self):  # Configuring what extensions will be used
        for exp in self.settings_files:  # Output about the configuration into the terminal
            if exp == "similarity":
                print("\t{0:9} | {1}".format(Fore.GREEN + exp, Fore.WHITE + str(self.settings_files[exp])))
            else:
                if self.settings_files[exp]:
                    print("\t{0:9} | ON".format(Fore.GREEN + exp))
                else:
                    print("\t{0:9} | OFF".format(Fore.RED + exp))

        print(Fore.WHITE)

        while True:  # Changing the configuration
            act = input('\tEnter "back" or "quit" to quit\nYou can add your own extension you need just writing it'
                        ' here\nThe extension to be changed: ').lower()

            if act in self.settings_files:
                if act == "similarity":
                    while True:
                        try:
                            number_similarity = int(input("Enter a nuber of similarity to change:"))
                            if 100 < number_similarity < 0:
                                print("You've entered a wrong number.")
                        except ValueError:
                            print("You've entered a wrong value.")
                        else:
                            self.settings_files["similarity"] = number_similarity
                            break
                else:
                    if self.settings_files[act]:
                        self.settings_files[act] = False
                    else:
                        self.settings_files[act] = True
                return
            elif act == "back" or act == "quit":
                return
            else:
                print(Fore.RED + '\nError! You entered the wrong file extension\n' + Fore.WHITE)

    def directory(self):  # Searches the desired line in all files in the directory
        while True:
            catalog_name = input('Enter "back" to exit\n\tDirectory path (C:/program): ').lower()

            if catalog_name == "back" or catalog_name == "quit":
                return

            find_str = input("\nText to find: ").lower()

            try:
                results = allFinder.search(catalog_name, find_str, self.settings_files)
                if not results:
                    print('\nThe text was not found. ;(\n')
                else:
                    for name_file, numbers_str, numbers_repeat in results:
                        print(f"\nPath to the file: {name_file}")
                        print(f'Content lines: {str(numbers_str).replace(",", " |")}')
                        print(f"String repetitions: {numbers_repeat}\n")
            except FileNotFoundError:
                print(Fore.RED + '\nError! You entered an invalid file path.\n' + Fore.WHITE)

    def run(self):  # Main function
        print('Press CTRL + C to quit.\n')

        while True:
            print("\nTo enter:\n[1] - Start")
            print("[2] - Settings of files extensions")

            inlet = input("Enter: ").lower()

            if inlet == "1":
                self.directory()
            elif inlet == "2":
                self.settings()
            else:
                print(Fore.RED + "Error! You entered the wrong command." + Fore.WHITE)


if __name__ == "__main__":  # Start!
    program = Main()
    program.run()
