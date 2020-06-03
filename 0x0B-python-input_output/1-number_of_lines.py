#!/usr/bin/python3
""" method to count file lines"""


def number_of_lines(filename=""):
    i = 0
    with open('{}'.format(filename)) as f:
        for line in f:
            i += 1
    return i
