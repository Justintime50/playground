# CHANGELOG

## v2.3.1 (2021-12-07)

* Adds `mypy` type checking

## v2.3.0 (2021-09-17)

* Removes support for Python 3.6
* Removes `mock` library and replaces it with builtin `unittest.mock` library
* Tweaks tests now that the assets directory has been removed

## v2.2.0 (2021-05-31)

* Added new phone/email searcher tool
* Moved dirs/files to ignore lists to constants in a separate file which can be reused by all tools in this repo
* Pins dependencies

## v2.1.0 (2021-02-04)

* Added Readmy Readmes tool
* Coverage report now also prints to console in addition to generating an HTML report

## v2.0.0 (2021-01-30)

* Changed name from `Gatekeeper` to `Rover IO` since most of the tools dealt with file and directory operations instead of protecting code.
* Added `Sequential Renamer` tool which sequentially and recursively renames files based on the folder they live in
* Switched from Travis CI to GitHub Actions
* Moved printing results to a separate function on all tools so we could properly assert outputs in tests while still maintaining console output for the real tool

## v1.1.0 (2020-09-15)

* Added unit tests and test coverage
* Scripts now properly return values
* Updated documentation
* Added a Makefile
* Rover IO Scout now prints the entire line your search query is found on instead of simply the search query (closes #4)
* Fixed a bug that could not properly open files based on encoding (closes #5)
* Additional code refactors to place everything into proper classes and functions
* Automated releasing via Travis

## v1.0.0 (2020-07-19)

* Published to PyPi and added setup.py
* Switched to argparse
* Cleaned up each script and documentation
* Added a new script that can search a directory for any string of text

## v0.2.0 (2020)

* Added a secrets search script that can search a directory for potential secrets that remain in code

## v0.1.0 (2020)

* Initial release
* Ability to search a directory for a set of files with the same file extension
