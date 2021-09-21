<div align="center">

# SMS To List

Send an SMS to individual numbers from a CSV on macOS.

[![Build Status](https://github.com/Justintime50/playground/workflows/build/badge.svg)](https://github.com/Justintime50/playground/actions)
[![Licence](https://img.shields.io/github/license/Justintime50/playground)](LICENSE)

<img src="https://raw.githubusercontent.com/justintime50/assets/main/src/sms-to-list/showcase.png" alt="Showcase">

</div>

SMS To List allows you to send an SMS to individual phone numbers from a CSV on macOS via the Messenger app. This works by calling a Python script that accepts a CSV file, iterates across those numbers, and calls an `Apple Script` that tells the `Messenger` app to send a text message from your real phone number to the list of recipients. This came about when my wife needed to send individualized text messages to a few dozen people and didn't want to spend the time copying and pasting the number and text message to each person while swapping the name.

## Install

```bash
# Install locally
make install

# Get Makefile help
make help
```

## Usage

SMS To List takes in a list of phone numbers and optional names (from a CSV), and a message (separate `message.py` file found in this project). You can customize the message to your liking and even personalize it to each recipient by passing an optional name `[NAME]` which gets replaced with the name associated with that number.

**NOTE:** You will most likely need to authorize your terminal to send text messages (macOS should prompt you on the first run).

```
Usage:
    venv/bin/python sms_to_list/send_sms.py --csv_file path/to/file.csv --force

Options:
    -h, --help            show this help message and exit
    -c CSV_FILE, --csv_file CSV_FILE
                            The path the CSV file containing names and numbers.
    -f, --force           Force sending the message, otherwise dry-run.
```

**CSV Format**

```
name,number
Justin,8015555555
Sarah,8015555555
Richard,8015555555
```

## Development

```bash
# Lint the project
make lint

# Run tests
make test

# Run test coverage
make coverage
```
