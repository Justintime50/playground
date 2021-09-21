import argparse
import csv
import os
import subprocess
import sys

from sms_to_list.message import MESSAGE


class SendSmsCli():
    def __init__(self):
        parser = argparse.ArgumentParser(
            description=(
                'Send an SMS to individual numbers from a CSV on macOS.'
            )
        )
        parser.add_argument(
            '-c',
            '--csv_file',
            required=True,
            help='The path the CSV file containing names and numbers.',
        )
        parser.add_argument(
            '-f',
            '--force',
            action='store_true',
            required=False,
            default=False,
            help='Force sending the message, otherwise dry-run.',
        )
        parser.parse_args(namespace=self)

    def run(self):
        SendSms.main(
            csv_file=self.csv_file,
            force=self.force
        )


class SendSms():
    def main(csv_file, force=False):
        """Take in a CSV of names/phone numbers
        """
        with open(csv_file, 'r') as csv_file_content:
            csv_reader = csv.DictReader(csv_file_content)

            for row in csv_reader:
                if row.get('name'):
                    message = MESSAGE.replace("[NAME]", row["name"]).replace('"', r'\"').strip()
                else:
                    message = MESSAGE.replace('"', r'\"').strip()
                current_path = os.path.abspath(os.path.dirname(sys.argv[0]))
                command = f'osascript {current_path}/send_sms.scpt {row["number"]} "{message}"'
                if force:
                    try:
                        subprocess.run(
                            command,
                            stdin=None,
                            stderr=None,
                            shell=True,
                            timeout=10
                        )
                        # TODO: Add check here for `Not authorized to send Apple events to Messages.` message
                        print(f'Message sent to {row["number"]}!')
                    except subprocess.TimeoutExpired:
                        raise Exception('Script timed out')
                    except subprocess.CalledProcessError as error:
                        raise Exception(f'Script error: {error}')
                else:
                    print(command)

        return command


if __name__ == '__main__':
    SendSmsCli().run()
