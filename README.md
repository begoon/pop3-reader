# Read POP3 mailbox and save all message to mbox

## Prerequisites

- python 3.8+

## Setup

    python -m venv ./.venv
    . ./.venv/bin/activate

    pip install -r requirements

## Usage

    python pop3_reader.py --help
    Usage: pop3_reader.py [OPTIONS]

    Options:
    --pop3_host TEXT  [required]
    --username TEXT   [required]
    --password TEXT   [required]
    --mbox-file TEXT  Output file for Mbox (default is inbox.mbox) [required]
    --commit          Skip performing QUIT command to keep messages "touched"
    --dry-run         Do not actually download messages
    --help            Show this message and exit.

## Example

    python pop3_reader.py --username=NAME --password=PASSWORD --dry-run
