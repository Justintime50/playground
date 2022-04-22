import argparse
import os
import re
from typing import List

from roverio.constants import DIRS_TO_IGNORE


class ScoutCLI:
    def __init__(self):
        parser = argparse.ArgumentParser(
            description='Scout searches through a directory for any string of text you specify.'
        )
        parser.add_argument(
            '-p',
            '--path',
            required=True,
            help='Where Scout will search for the string specified in each file.',
        )
        parser.add_argument(
            '-s',
            '--search',
            required=True,
            help='The string to search for in each file of a path.',
        )
        parser.parse_args(namespace=self)

    def run(self):
        Scout.main(
            path=self.path,
            search=self.search,
        )


class Scout:
    @staticmethod
    def main(path: str, search: str):
        """Run the tool and print to console."""
        print('\n##################\nROVER IO - SCOUT\n##################\n')
        print('Rover IO Scout found the following for your search query:\n')
        messages = Scout.search_for_string(path, search)
        for message in messages:
            print(message)

    @staticmethod
    def search_for_string(path: str, search: str) -> List[str]:
        """Iterate over each file and directory and build a list of results
        containing the specified string.
        """
        regex_pattern = re.compile(search)

        # Scout for the search query in all subdirectories of the one specified
        scout_files = []
        for root, dirs, files in os.walk(path, topdown=True):
            dirs[:] = [directory for directory in dirs if directory not in DIRS_TO_IGNORE]
            for filename in files:
                filepath = os.path.join(root, filename)

                # Open each file and print the findings
                with open(filepath, 'r') as single_file:
                    for line_number, line in enumerate(single_file, 1):
                        data = regex_pattern.findall(line)
                        for search in data:
                            message = f'File: {filepath}\nSearch: {line.strip()}\nLine: {line_number}\n'
                            scout_files.append(message)

        return scout_files


def main():
    ScoutCLI().run()


if __name__ == '__main__':
    main()
