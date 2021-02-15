# Finder-in-files
**This script searches for a specific string across all files in the directory you specified**
## Supported file formats for searching
- txt
- log
- html
- css
- cpp
- h
- js
- py
- c
### Special formats
- doc
- docx
- otd
- rtf  (May not work on Windows)
- pdf  (May not work on Windows)

## Documentation

### Installation

```
Poka net
```

### Import
To import a module into your code use:
```
import finder_in_files as finder
```
### Usage
To find a line in files in a directory, use:
```
finder.search(catalog_name, find_str, settings_files=DEFAULT_SETTINGS_FILES)
```
`catalog_name` - The name of the directory where the search should be performed.

`find_str` - Search string.

`settings_files` - Setting file extensions (enable / disable).

`DEFAULT_SETTINGS_FILES` -
 
 ```
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
```
The search is performed on the lines of the file. If `find_str` is more than 89% similar to a line in the file, the line is considered found.

The `search` function returns a tuple (name_file, numbers_str numbers_repeat).

`name_file` - The path to the file where `find_str` was found.

`numbers_str` - Returned as a list that consists of the lines where `find_str` was found.

`numbers_repeat` - The number of times to repeat `find_str` in the file. Returned in int format.

## Example
An example where all of this is used together.

```
try:
                results = finder_in_files.search(catalog_name, find_str, self.settings_files)
                if not results:  # If nothing was found, then
                    print('\nThe text was not found. ;(\n')
                else:
                    for name_file, numbers_str, numbers_repeat in results:  # We unpack the tuple using for.
                        print(f"\nPath to the file: {name_file}")
                        print(f'Content lines: {str(numbers_str).replace(",", " |")}')
                        print(f"String repetitions: {numbers_repeat}\n")
            except FileNotFoundError:  # print('\nError! You entered an invalid file path.')  
            # An exception if the path (catalog_name) was not specified correctly.
```
