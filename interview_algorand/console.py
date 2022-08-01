#!/bin/env python3

import argparse
import logging
import json
import sys

from interview_algorand import config
from interview_algorand import github


class ConsoleDisplay:

    def __init__(self, settings: config.Settings):
        """Initialize the console display."""
        self.logger = logging.getLogger(__name__)
        self.settings = settings

    def display(self):
        """Display the issues for the given repo."""
        self.logger.debug("Retrieving issues")
        issues = github.get_issues(self.settings)
        json.dump(issues, fp=sys.stdout)


def parse_args() -> argparse.Namespace:
    """Parse the command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true')
    parser.add_argument('--repo', default='algorand/go-algorand')
    return parser.parse_args()


def setup_logging(args: argparse.Namespace):
    """Setup the logging."""
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)


def run():
    """Run the program."""
    args = parse_args()
    settings = config.get_config(args)
    display = ConsoleDisplay(settings)
    display.display()


if __name__ == '__main__':
    run()
