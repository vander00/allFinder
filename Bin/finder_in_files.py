import os
import textract
from fuzzywuzzy import fuzz

results = list()


class Settings:
    DEFAULT_SETTINGS_FILES = {
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

    SIMPLE_EXTENSIONS = ["txt", 'log', 'html', 'css', 'cpp', 'h', 'js', 'py', 'c']  # Supported file formats
    COMPLICATED_EXTENSIONS = ['doc', 'docx', 'odt', 'pdf', 'rtf']  # Need a library to read


def _checker_default(catalog_name, find_str, name_file):
    # ---Data---
    numbers_str = list()  # Lines with text
    number_str = 1  # The line where the text was found
    numbers_repeat = 0  # Repeating text in a file

    with open(catalog_name + "/" + name_file, 'r', encoding='utf-8') as f:  # Opening a file
        for line in f:
            # If the line matches more than 88%, the information gets displayed
            if fuzz.partial_ratio(find_str, line.lower()) > 88:
                numbers_repeat += 1
                numbers_str.append(number_str)
                number_str = 0
            number_str += 1
        if numbers_repeat != 0:
            return catalog_name + '/' + name_file, str(numbers_str).replace(",", " |"), numbers_repeat

        return False


def _checker_other(catalog_name, find_str, name_file):
    # ---Data---
    numbers_str = list()  # Lines with text
    number_str = 1  # The line where the text was found
    numbers_repeat = 0  # Repeating text in a file
    try:  # File validation check
        f = textract.process(catalog_name + "/" + name_file).decode('utf-8').lower().split('\n')
        for line in f:
            # If the line matches more than 88%, then the information is displayed
            if fuzz.partial_ratio(find_str, line) > 88:
                numbers_repeat += 1
                numbers_str.append(number_str)
                number_str = 0
            number_str += 1
            if numbers_repeat != 0:
                return catalog_name + '/' + name_file, str(numbers_str).replace(",", " |"), numbers_repeat

        return False
    except (KeyError, Exception):
        pass


def search(catalog_name, find_str, settings_files=None):  # To find out the directory
    if settings_files is None:
        settings_files = Settings.DEFAULT_SETTINGS_FILES
    if not os.path.exists(catalog_name):
        raise FileNotFoundError(f'Directory "{catalog_name}" not found.')

    find_str = str(find_str)

    catalog = os.listdir(catalog_name)
    for name in catalog:
        if name.split('.')[-1] in Settings.SIMPLE_EXTENSIONS:
            if settings_files[name.split('.')[-1]]:
                res = _checker_default(catalog_name, find_str, name)
                if res:
                    results.append(res)
        elif name.split('.')[-1] in Settings.COMPLICATED_EXTENSIONS:
            if settings_files[name.split('.')[-1]]:
                res = _checker_other(catalog_name, find_str, name)
                if res:
                    results.append(res)

    return results
