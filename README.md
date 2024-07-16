# CSV to JSON Converter

This is a Python script that converts CSV files to JSON format. It supports automatic encoding detection, recursive directory traversal, and various customization options for the output JSON.

## Features

- Convert individual CSV files to JSON.
- Convert all CSV files in a directory (with optional recursion into subdirectories).
- Automatically detect the encoding of CSV files.
- Option to prevent overwriting existing JSON files.
- Option to output compact JSON (not pretty-printed).
- Verbose mode for detailed output.

## Requirements

- Python 3.x
- `chardet` library

## You have to install required library for automatic file extension or encode detection using pip:

pip install chardet

## Usage

## Command Line -h or help Arguments
python .\csv-to-json-converter.py -h
<br>usage: csv-to-json-converter.py [-h] [-o OUTPUT] [-v] [-r] [--no-overwrite] [-e ENCODING] [--compact] path

Convert CSV files to JSON

positional arguments:
  path                  File or directory path

```options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output directory for JSON files
  -v, --verbose         Enable verbose output
  -r, --recursive       Recursively search for CSV files in subdirectories
  --no-overwrite        Do not overwrite existing JSON files
  -e ENCODING, --encoding ENCODING
                        Specify input CSV file encoding (default: auto-detect)
  --compact             Output compact JSON (not pretty-printed)
```
# Examples
## Convert a Single CSV File
python csv-to-json-converter.py sample.csv
<br>or<br>
python csv-to-json-converter.py path/to/file.csv -o path/to/output

## Convert All CSV Files in a Directory
python csv-to-json-converter.py path/to/directory -o path/to/output

## Convert All CSV Files in a Directory Recursively
python csv-to-json-converter.py path/to/directory -o path/to/output -r

## Convert with Verbose Output and No Overwrite
python csv-to-json-converter.py path/to/file.csv -o path/to/output -e utf-8 --compact

## Convert with Specified Encoding and Compact JSON
python csv-to-json-converter.py path/to/file.csv -o path/to/output -e utf-8 --compact

## sample file and result
sample.csv 
sample.json


## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Author
Created by [_dinoherlambang_](https://instagram.com/_dinoherlambang_/)
