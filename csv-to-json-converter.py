import csv
import json
import os
import argparse
import sys
import chardet
from pathlib import Path

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw = file.read()
    return chardet.detect(raw)['encoding']

def csv_to_json(csv_file_path, json_file_path, encoding='utf-8', indent=None):
    data = []
    with open(csv_file_path, 'r', encoding=encoding) as csv_file:
        dialect = csv.Sniffer().sniff(csv_file.read(1024))
        csv_file.seek(0)
        csv_reader = csv.DictReader(csv_file, dialect=dialect)
        for row in csv_reader:
            data.append(row)

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=indent, ensure_ascii=False)

def convert_file(file_path, output_dir, verbose, no_overwrite, encoding, compact):
    if not file_path.lower().endswith('.csv'):
        if verbose:
            print(f"Warning: {file_path} is not a CSV file. Skipping.")
        return

    if encoding == 'auto':
        encoding = detect_encoding(file_path)
        if verbose:
            print(f"Detected encoding for {file_path}: {encoding}")

    output_path = Path(output_dir) / (Path(file_path).stem + ".json")
    
    if output_path.exists() and no_overwrite:
        print(f"Warning: {output_path} already exists. Skipping due to --no-overwrite option.")
        return

    indent = None if compact else 4
    csv_to_json(file_path, output_path, encoding, indent)
    
    if verbose:
        print(f"Converted {file_path} to {output_path}")

def convert_multiple_files(directory, output_dir, verbose, recursive, no_overwrite, encoding, compact):
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.lower().endswith('.csv'):
                file_path = Path(root) / filename
                convert_file(str(file_path), output_dir, verbose, no_overwrite, encoding, compact)
        if not recursive:
            break

def main():
    parser = argparse.ArgumentParser(description="Convert CSV files to JSON")
    parser.add_argument("path", help="File or directory path")
    parser.add_argument("-o", "--output", help="Output directory for JSON files", default=".")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("-r", "--recursive", action="store_true", help="Recursively search for CSV files in subdirectories")
    parser.add_argument("--no-overwrite", action="store_true", help="Do not overwrite existing JSON files")
    parser.add_argument("-e", "--encoding", default="auto", help="Specify input CSV file encoding (default: auto-detect)")
    parser.add_argument("--compact", action="store_true", help="Output compact JSON (not pretty-printed)")

    args = parser.parse_args()

    if os.path.isfile(args.path):
        convert_file(args.path, args.output, args.verbose, args.no_overwrite, args.encoding, args.compact)
    elif os.path.isdir(args.path):
        convert_multiple_files(args.path, args.output, args.verbose, args.recursive, args.no_overwrite, args.encoding, args.compact)
    else:
        print(f"Error: {args.path} is not a valid file or directory")
        sys.exit(1)

if __name__ == "__main__":
    main()
