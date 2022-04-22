<div align="center">

# Rover IO

Rover IO is a suite of tools that traverses your directories and performs IO file operations.

[![Build Status](https://github.com/Justintime50/roverio/workflows/build/badge.svg)](https://github.com/Justintime50/roverio/actions)
[![Coverage Status](https://coveralls.io/repos/github/Justintime50/roverio/badge.svg?branch=main)](https://coveralls.io/github/Justintime50/roverio?branch=main)
[![PyPi](https://img.shields.io/pypi/v/roverio)](https://pypi.org/project/roverio/)
[![Licence](https://img.shields.io/github/license/justintime50/roverio)](LICENSE)

<img src="https://raw.githubusercontent.com/justintime50/assets/main/src/roverio/showcase.png" alt="Showcase">

</div>

Rover IO is the perfect companion to any source control workflow. Find files still containing secrets or search for specific file types or strings of characters you may have forgotten to add to your gitignore. Rename massive collections of files sequentially and recursively (perfect for something like a photo library).

## Install

```bash
# Install tool
pip3 install roverio

# Install locally
make install
```

## Usage

### File Extension

File Extension searches for all files in a path with the specified file extension and returns all the specified results.

```
Usage:
    roverio-file-extension --path ~/code/my_project --extension ".py"

Options:
    -h, --help                              show this help message and exit
    -p PATH, --path PATH                    Where File Extension will search for files with the specified file extension.
    -e EXTENSION, --extension EXTENSION     The file extension to search a path for.
```

### Phone Email Searcher

Phone Email Searcher searches for files that may contain phone numbers or email addresses.

```
Usage:
    roverio-phone-email-searcher --path ~/code/my_project --phone --email

Options:
    -h, --help   show this help message and exit
    --path PATH  Where Phone/Email Searcher will search.
    -p, --phone  Search for phone numbers in the directory specified.
    -e, --email  Search for emails in the directory specified.
```

### Readmy Readmes

Readmy Readmes is a fantastic tool to help find the holes in your project's documentation. Quickly iterate over every project README you have to search for key phrases you know should be there. 

Each rule must be on its own line in your `rules` test file. Depending on the path you specify, you can search all your project README's or just a single project.

**Use Cases**
* Ensure you have instructions for installing, usage, and testing your project
* Find long-forgotten TODO's that still need fixing
* Search for a particular phrase when you can't remember where it lived
* Find hiding README's deep in a project's structure

```
Usage
    roverio-readmy-readmes -p path/to/git_projects -r path/to/rules.txt -l -c -csv_path path/to/file.csv

Options:
    -h, --help            show this help message and exit
    -p PATH, --path PATH  The path where the tool will search for README's.
    -r RULES, --rules RULES
                            The path to your rule text file.
    -l, --lazy            Match rules lazily (case-insensitive).
    -c, --create_csv      Save output to a CSV file.
    --csv_path CSV_PATH   The file path where a CSV file will be saved. By default, it will be saved to the current directory.
```

**Sample Output**

```
| README File             | install | usage | test  | todo  |
| ----------------------- | ------- | ----- | ----- | ----- |
| adventofcode/README.md  | True    | True  | True  | False |
| algorithms/README.md    | True    | True  | True  | False |
| brew-backup/README.md   | True    | True  | False | False |
| brew-update/README.md   | False   | True  | False | False |
| build-project/README.md | True    | True  | False | False |
| build-readme/README.md  | True    | True  | True  | False |
| burn-notice/README.md   | False   | True  | False | False |
| dad/README.md           | True    | True  | True  | False |
| dev-tools/README.md     | False   | True  | True  | False |
| diff/README.md          | True    | True  | True  | False |
| dotfiles/README.md      | True    | True  | False | False |
...
```

### Scout

Scout searches through a directory for any string of text you specify. Perfect for searching across multiple projects or large code bases.

```
Usage:
    roverio-scout --path ~/code/my_project --search "My string of text"

Options:
    -h, --help                  show this help message and exit
    -p PATH, --path PATH        Where Scout will search for the string specified in each file.
    -s SEARCH, --search SEARCH  The string to search for in each file of a path.
```

### Secrets

Secrets searches a path for possible secrets in code. Perfect for finding any passwords, API keys, or secrets you were about to commit. This is accomplished through loose searching of strings of a certain length and is not foolproof in determining what an actual secret is vs a long string.

```
Usage:
    roverio-secrets --path ~/code/my_project --length 20

Options:
    -h, --help                    show this help message and exit
    -p PATH, --path PATH          Where Secrets will search for the string specified in each file.
    -l LENGTH, --length LENGTH    The minimum length of the secrets to search for.
```

### Sequential Renamer

Sequential Renamer recursively renames files in a directory in a sequential manner and prepends the parent folder name. The filename is slugified and lowercased for a uniform naming scheme.

A perfect use case for Seqential Renamer is a large photo library where filenames may be all over the place such as `IMG_1234.JPG` and you want them renamed according to folder. This script has been tested with a library of `10,000` photos.

```
Usage:
    roverio-sequential-renamer --path ~/path/to/photos --force

Options:
    -h, --help            show this help message and exit
    -p PATH, --path PATH  Where Sequential Renamer will recursively rename files it finds.
    -f, --force           Force changes which take permenant effect.
```

**Sample Output**

```
/Users/jhammond/Downloads/Justin's Skydive 2019/IMG_2462_proc_592015324.JPG  ->  justins-skydive-2019-0.jpg
/Users/jhammond/Downloads/Justin's Skydive 2019/IMG_2494_proc_592015326.JPG  ->  justins-skydive-2019-1.jpg
/Users/jhammond/Downloads/Justin's Skydive 2019/IMG_2514_proc_592015327.JPG  ->  justins-skydive-2019-2.jpg
```

## Development

```bash
# Get a comprehensive list of development tools
make help

# Run the scripts locally
venv/bin/python roverio/secrets.py --help
```
