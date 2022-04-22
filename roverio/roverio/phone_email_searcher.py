import argparse
import os
import re
from typing import List

from roverio.constants import DIRS_TO_IGNORE, FILES_TO_IGNORE


class PhoneEmailSearcherCli:
    def __init__(self):
        parser = argparse.ArgumentParser(
            description='Phone/Email Searcher recursively searches files for patterns that may match a phone or email.'
        )
        parser.add_argument(
            '--path',
            required=True,
            help='Where Phone/Email Searcher will search.',
        )
        parser.add_argument(
            '-p',
            '--phone',
            required=False,
            action='store_true',
            help='Search for phone numbers in the directory specified.',
        )
        parser.add_argument(
            '-e',
            '--email',
            required=False,
            action='store_true',
            help='Search for emails in the directory specified.',
        )
        parser.parse_args(namespace=self)

    def run(self):
        PhoneEmailSearcher.main(
            path=self.path,
            phone=self.phone,
            email=self.email,
        )


class PhoneEmailSearcher:
    @staticmethod
    def main(path: str, phone: str, email: str):
        """Run the tool and print results to console."""
        if phone:
            phone_results = PhoneEmailSearcher.search_for_phone(path)
            for result in phone_results:
                print(result)
        if email:
            email_results = PhoneEmailSearcher.search_for_email(path)
            for result in email_results:
                print(result)

    @staticmethod
    def search_for_phone(path: str) -> List[str]:
        """Search for files that may contain a phone number."""
        # Matches a phone number as simple as `8015551234` or as complex as `+44 (801) 555-1234`
        # This is most likely too loose of a regex, but very forgiving and will catch weird edge cases
        phone_regex = re.compile(r'[0-9-+() ]{10,18}')

        # Scout for the search query in all subdirectories of the one specified
        phone_files = []
        for root, dirs, files in os.walk(path, topdown=True):
            dirs[:] = [directory for directory in dirs if directory not in DIRS_TO_IGNORE]
            for filename in files:
                filepath = os.path.join(root, filename)

                # Open each file and print the findings
                _, file_extension = os.path.splitext(filepath)
                if file_extension.lower() not in FILES_TO_IGNORE:
                    with open(filepath, 'r') as single_file:
                        for line_number, line in enumerate(single_file, 1):
                            data = phone_regex.findall(line)
                            for result in data:
                                if any(char.isdigit() for char in result):
                                    message = f'File: {filepath}\nResult: {line.strip()}\nLine: {line_number}\n'
                                    phone_files.append(message)

        return phone_files

    @staticmethod
    def search_for_email(path: str) -> List[str]:
        """Search for files that may contain an email."""
        # Losely matches email patterns of `anything@anything.anything` without spaces
        email_regex = re.compile(r'[^\s]+@[^\s]+\.[^\s]+')

        # Scout for the search query in all subdirectories of the one specified
        email_files = []
        for root, dirs, files in os.walk(path, topdown=True):
            dirs[:] = [directory for directory in dirs if directory not in DIRS_TO_IGNORE]
            for filename in files:
                filepath = os.path.join(root, filename)

                # Open each file and print the findings
                _, file_extension = os.path.splitext(filepath)
                if file_extension.lower() not in FILES_TO_IGNORE:
                    with open(filepath, 'r') as single_file:
                        for line_number, line in enumerate(single_file, 1):
                            data = email_regex.findall(line)
                            for result in data:
                                # Don't accidentally grab massive strings that aren't emails
                                if len(line) < 256:
                                    message = f'File: {filepath}\nResult: {line.strip()}\nLine: {line_number}\n'
                                    email_files.append(message)

        return email_files


def main():
    PhoneEmailSearcherCli().run()


if __name__ == '__main__':
    main()
