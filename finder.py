import os
import textract
from fuzzywuzzy import fuzz


class Finder:
    # --- Data ---
    FILES_NAMES = [["txt", 'log', 'html', 'css', 'cpp', 'h', 'js', 'py', 'c'], ['doc', 'docx', 'rtf', 'odt']]

    def __init__(self):
            self.feeling = True
    
    def checker_default(self, catalog_name, find_str, name_file):
        # ---Data---
        numbers_str = list()
        number_str = 1
        numbers_repeat = 0
        self.feeling = True

        with open(catalog_name + "/" + name_file, 'r', encoding='utf-8') as f:
            for line in f:
                if fuzz.partial_ratio(find_str, line) > 88:
                    self.feeling = False
                    numbers_repeat += 1
                    numbers_str.append(number_str)
                    number_str = 0
                number_str += 1
            if self.feeling == False:
                print(f"\nПуть к файлу: {catalog_name + '/' + name_file}.")
                print(f'Строки содержания: {str(numbers_str).replace(",", " |")}')
                print(f"Повторений в файле: {numbers_repeat}")

    def checker_other(self, catalog_name, find_str, name_file):
        if find_str in textract.process(catalog_name + "/" + name_file).decode('utf-8').lower():
            self.feeling = False
            print(f"Путь к файлу: {catalog_name + '/' + name_file}")

    def run(self):
        while True:
            catalog_name = input("Введите путь к каталогу: ")
            find_str = input("\nЧто бы Вы хотели найти?: ").lower()
            
            try:
                catalog = os.listdir(catalog_name)
                for name in catalog:
                    if name.split('.')[-1] in Finder.FILES_NAMES[0]:
                        self.checker_default(catalog_name, find_str, name)
                    elif name.split('.')[-1] in Finder.FILES_NAMES[1]:
                        self.checker_other(catalog_name, find_str, name)
                if self.feeling == True:
                    print("Объект не был найден. ;(")
            except FileNotFoundError:
                print('\nОшибка! Вы ввели неверную деректорию.')


if __name__ == "__main__":
    program = Finder()
    program.run()
