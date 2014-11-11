#!/usr/bin/python3
# coding=utf-8
"""
Regex Tutorial
https://www.youtube.com/watch?v=hiDg2TFYL9E&index=1&list=WL
"""

__author__ = "Michael Krisper"
__email__ = "michael.krisper@gmail.com"
__date__ = "2014-11-11"

import re

def main():
    """
    .     single char
    [ ]   all in brackets
    [^ ]  all not in brackets
    ^     at start of string
    $     at end of string
    (  )  sub expressions
    *     zero or more
    ?     zero or one
    +     one or more

    match()    -  match from start of string
    search()   -  anywhere in the string
    fullmatch() - match whole string
    """
    line = "I think I understand regular expressions"
    match_result = re.match(r"think", line, re.M|re.I)
    if match_result:
        print("match found: {}".format(match_result.group()))
    else:
        print("no match was found.")

    search_result = re.search(r"think", line, re.M|re.I)
    if search_result:
        print("search found: {}".format(search_result.group()))
    else:
        print("no search was found.")


if __name__ == "__main__":
    main()