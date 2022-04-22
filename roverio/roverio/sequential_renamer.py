import argparse
import os
import re
from typing import List, Tuple


class SequentialRenamerCLI:
    def __init__(self):
        parser = argparse.ArgumentParser(
            description='Sequential Renamer recursively renames files in a directory in a sequential manner and prepends the parent folder name.'  # noqa
        )
        parser.add_argument(
            '-p',
            '--path',
            required=True,
            help='Where Sequential Renamer will recursively rename files it finds.',
        )
        parser.add_argument(
            '-f',
            '--force',
            required=False,
            action='store_true',
            help='Force changes which take permenant effect.',
        )
        parser.parse_args(namespace=self)

    def run(self):
        SequentialRenamer.main(
            path=self.path,
            force=self.force,
        )


class SequentialRenamer:
    @staticmethod
    def main(path: str, force: bool = False):
        """Run the tool printing the results to console."""
        print(
            'Sequential Renamer in progress, this could take awhile depending on the number of items in your specified'
            ' path...'
        )
        messages, files_updated = SequentialRenamer.rename_files(path, force)
        if force:
            print(f'Process complete, {files_updated} records were updated!')
        else:
            for message in messages:
                print(message)
            print(f'{files_updated} records will be updated when forced.')
            print('DRY RUN complete, run with the "--force" flag to actually rename files.')

    @staticmethod
    def rename_files(path: str, force: bool = False) -> Tuple[List[str], int]:
        """Recursively rename files in a sequential manner, prepending the folder name to
        a seqential number that restarts in each folder.

        Example output:
        /Users/jhammond/Downloads/Justin Skydive 2019/IMG_2462_proc_592015324.jpg  ->  justin-skydive-2019-0.jpg
        /Users/jhammond/Downloads/Justin Skydive 2019/IMG_2494_proc_592015326.jpg  ->  justin-skydive-2019-1.jpg
        /Users/jhammond/Downloads/Justin Skydive 2019/IMG_2514_proc_592015327.jpg  ->  justin-skydive-2019-2.jpg
        """  # noqa
        files_to_ignore = [
            '.ds_store',
        ]
        dirs_to_ignore = [
            'photos library',
            'photos library.photoslibrary',
        ]

        files_updated = 0
        messages = []
        for root, dirs, files in os.walk(path, topdown=True):
            files[:] = [filename for filename in files if filename.lower() not in files_to_ignore]
            dirs[:] = [directory for directory in dirs if directory.lower() not in dirs_to_ignore]
            for i, full_filename in enumerate(files):
                file_extension = os.path.splitext(full_filename)[1].lower()

                folder_name = os.path.basename(os.path.dirname(os.path.join(root, full_filename)))
                slugged_folder_name = folder_name.replace('_', '-').replace(' ', '-')

                files_updated += 1
                new_filename = (
                    re.sub(r'[^0-9a-zA-Z-_]+', '', slugged_folder_name) + '-' + str(i) + file_extension
                ).lower()
                messages.append(os.path.join(root, full_filename) + '  ->  ' + new_filename)

                if force:
                    os.rename(os.path.join(root, full_filename), os.path.join(root, new_filename))
            print(messages)

        return messages, files_updated


def main():
    SequentialRenamerCLI().run()


if __name__ == '__main__':
    main()
