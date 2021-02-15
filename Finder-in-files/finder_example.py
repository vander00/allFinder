import finder_in_files
from colorama import Fore  # pip install colorama


class Test:
    def __init__(self):
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
            'odt': True,
            'pdf': True
        }

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

            find_str = input("\nText to find: ").lower()

            try:
                results = finder_in_files.search(catalog_name, find_str, self.settings_files)
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
            print("[2] - Setting File extensions")

            inlet = input("Enter: ").lower()

            if inlet == "1":
                self.directory()
            elif inlet == "2":
                self.settings()
            else:
                print(Fore.RED + "Error! You entered the wrong command." + Fore.WHITE)


if __name__ == "__main__":  # Start!
    program = Test()
    program.run()
