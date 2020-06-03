#!/usr/bin/python3
"""Defintion of append after function"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line
    containing a specific string"""
    string = ""
    with open(filename) as f:
        for line in f:
            string += line
            if search_string in line:
                string += new_string
    with open(filename, 'w') as f:
        f.write(t)
