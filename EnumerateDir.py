import argparse
import os
import sys
import re


def error(message):
    print('Error: ' + message)


def main():
    parser = argparse.ArgumentParser(description='Enumerate the content of a directory')
    parser.add_argument('-e', '--extensions', action='store_true', help='Include file extensions')
    parser.add_argument('path', type=str, nargs='?', default='.', help='Directory to enumerate')
    parser.add_argument('output', type=str, nargs='?', help='Path of output')

    args = parser.parse_args()
    root_path = os.path.abspath(args.path)
    output_path = os.path.abspath(args.output) if args.output else os.path.join(os.path.abspath('.'), 'Output.txt')

    if not os.path.isdir(root_path):
        error(f'Directory to enumerate {root_path} does not exist.')
        sys.exit(1)

    print(f"Enumerating '{root_path}' to '{output_path}'{' with extensions' if args.extensions else ''}")

    date_regex = r'\d{4}-\d{2}-\d{2}'

    with open(output_path, mode='w', encoding='utf') as output_file:
        output_file.write(f'{root_path}\n')

        for dir_path, dir_names, file_names in os.walk(root_path):
            relative_path = str(os.path.relpath(dir_path, root_path))
            if 'Exposure' in relative_path:
                continue

            match = re.search(date_regex, relative_path)
            if not match:
                continue

            dir_date = match.group() if match else None

            for file_name in file_names:
                name, extension = os.path.splitext(file_name)
                file_date = file_name[:4] + '-' + file_name[4:6] + '-' + file_name[6:8]
                file_output = file_name if args.extensions else name
                mismatch_output = "" if file_date in dir_date else " 'NAME MISMATCH'"

                output_file.write(f"'{relative_path}' '{file_output}'{mismatch_output}\n")


if __name__ == '__main__':
    main()
