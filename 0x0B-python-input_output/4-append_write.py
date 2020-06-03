#!/usr/bin/python3
""" define function write_append"""


def append_write(filename="", text=""):
    """ append text to a file """

    with open(filename, 'a') as f:
        return f.write(text)
