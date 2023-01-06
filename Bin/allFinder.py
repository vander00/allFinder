import os
import textract
from fuzzywuzzy import fuzz


class DefaultSettings:
    DEFAULT_SETTINGS_FILES = {
        'doc': True,
        'docx': True,
        'rtf': True,
        'odt': True,
        'pdf': True,
        'similarity': 88,
    }

    COMPLICATED_EXTENSIONS = ['doc', 'docx', 'odt', 'pdf', 'rtf']  # Need library to read


# Function which is able to read simple data files
def _checker_default(catalog_name, desired_string, file_name, similarity):
    # ---Data---
    numbers_str = list()  # Lines with text
    number_str = 1  # The line where the text was found
    numbers_repeat = 0  # Repeating text in the file

    with open(catalog_name + "/" + file_name, 'r', encoding='utf-8') as f:  # Opening a file
        for line in f:
            # If the line matches more than similarity, the information gets displayed
            if fuzz.partial_ratio(desired_string, line.lower()) > similarity:
                numbers_repeat += 1
                numbers_str.append(number_str)
                number_str = 0
            number_str += 1
        if numbers_repeat != 0:
            return catalog_name + '/' + file_name, str(numbers_str).replace(",", " |"), numbers_repeat

        return False


def _checker_complicated(catalog_name, desired_string, file_name, similarity):
    # ---Data---
    numbers_str = list()  # Lines with text
    number_str = 1  # The line where the text was found
    numbers_repeat = 0  # Repeating text in a file
    try:  # File validation check
        f = textract.process(catalog_name + "/" + file_name).decode('utf-8').lower().split('\n')
        for line in f:
            # If the line matches more than similarity, then the information is displayed
            if fuzz.partial_ratio(desired_string, line) > similarity:
                numbers_repeat += 1
                numbers_str.append(number_str)
                number_str = 0
            number_str += 1
            if numbers_repeat != 0:
                return catalog_name + '/' + file_name, str(numbers_str).replace(",", " |"), numbers_repeat

        return False
    except (KeyError, Exception):
        pass


def search(catalog_name, desired_string, files_settings=None):  # Finds the needed directory
    results = list()  # List storing all suitable information for the user

    if files_settings is None:
        files_settings = DefaultSettings.DEFAULT_SETTINGS_FILES
    if not os.path.exists(catalog_name):
        raise FileNotFoundError(f'Directory "{catalog_name}" not found.')

    desired_string = str(desired_string)

    catalog = os.listdir(catalog_name)
    for name in catalog:
        # Checks if the extension must be read by textract library
        if name.split('.')[-1] in DefaultSettings.COMPLICATED_EXTENSIONS:
            if files_settings[name.split('.')[-1]]:
                res = _checker_complicated(catalog_name, desired_string, name, files_settings["similarity"])
                if res:
                    results.append(res)
        else:
            if files_settings[name.split('.')[-1]]:
                res = _checker_default(catalog_name, desired_string, name, files_settings["similarity"])
                if res:
                    results.append(res)
    return results
