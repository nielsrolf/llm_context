import argparse
import os
import glob

def concatenate_files(paths, extensions=None):
    for path in paths:
        # If path is a directory, recursively add all files within it that match the extensions filter
        if os.path.isdir(path):
            if extensions:
                for ext in extensions:
                    for filename in glob.glob(os.path.join(path, '**', f'*{ext}'), recursive=True):
                        print_file_content(filename)
            else:
                for root, _, files in os.walk(path):
                    for filename in files:
                        print_file_content(os.path.join(root, filename))
        # If path is a file, simply print its content (if it matches the extensions filter, if one is provided)
        elif os.path.isfile(path):
            if not extensions or any(path.endswith(ext) for ext in extensions):
                print_file_content(path)

def print_file_content(filepath):
    print(f'# --- file: {filepath}')
    with open(filepath, 'r') as file:
        print(file.read())

def main():
    parser = argparse.ArgumentParser(description='Concatenate files from given directories and/or file paths.')
    parser.add_argument('paths', type=str, nargs='+', help='Directories and/or file paths to concatenate.')
    parser.add_argument('--ext', type=str, nargs='*', help='Optional list of file extensions to filter by.')
    args = parser.parse_args()

    concatenate_files(args.paths, extensions=args.ext)

if __name__ == '__main__':
    main()
