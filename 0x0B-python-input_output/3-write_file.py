#!/usr/bin/python3
""" define write_file function """


def write_file(filename="", text=""):
    """ Write in a file """

    with open(filename, 'w') as f:
        return f.write(text)
