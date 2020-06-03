#!/usr/bin/python3
""" Function to read file """


def read_file(filename=""):
    """ reading from file function """

    with open('{}'.format(filename)) as f:
        print(f.read(), end="")
