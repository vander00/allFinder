# AllFinder
**This script searches for a specific string across all files in the directory you specified**
## Supported special formats
- doc
- docx
- otd
- rtf  (May not work on Windows)
- pdf  (May not work on Windows)

## Documentation

### Installation

You can just download the `allFinder` file and import it in your project.

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
        'doc': True,
        'docx': True,
        'rtf': True,
        'odt': True,
        'pdf': True
}
```
The search is performed on the lines of the file. If `find_str` is more than 89% similar to a line in the file, the line is considered found.
If you want, you can any extension you want just adding the name into the dictionary.

The `search` function returns a tuple (file_name, str_numbers, repeats_number).

`file_name` - The path to the file where `desired_str` was found.

`str_numbers` - Returned as a list that consists of the lines where `desired_str` was found.

`repeats_number` - The number how many times `desired_str` was repeated in the file. Returned in int format.

## Example
An example where everything is used altogether.

```
try:
    results = allFinder.search(catalog_name, find_str, self.settings_files)
    if not results:
        print('\nThe text was not found. ;(\n')
    else:
        for name_file, numbers_str, numbers_repeat in results:
            print(f"\nPath to the file: {name_file}")
            print(f'Content lines: {str(numbers_str).replace(",", " |")}')
            print(f"String repetitions: {numbers_repeat}\n")
except FileNotFoundError 
    print('\nError! You entered an invalid file path.')  
```

If you want a much more full example about the library check `example` folder of the repository.