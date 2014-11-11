#! /usr/bin/env python3
# coding=utf-8
"""
Find a regex pattern in a file.

Inspired by tutorial: https://www.youtube.com/watch?v=hiDg2TFYL9E&list=WL#t=589
"""

__author__ = "Michael Krisper"
__email__ = "michael.krisper@gmail.com"
__date__ = "2014-11-11"

import re
import sys
import argparse


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(dest="word", help="specify a word to search for")
    parser.add_argument("-f", dest="filename", help="specify a file to search. If this arguments is omitted, the stdin is used.")

    args = parser.parse_args()

    if args.filename:
        try:
            search_file = open(args.filename)
        except IOError as e:
            print("File could not be opened: {}".format(e))
            return
    else:
        search_file = sys.stdin

    reg = re.compile(args.word)

    try:
        for linenr, line in enumerate(search_file, start=1):
            search_result = reg.search(line)
            if search_result:
                print("{}: {}".format(linenr, line.rstrip("\n")))
    finally:
        search_file.close()


if __name__ == "__main__":
    main()