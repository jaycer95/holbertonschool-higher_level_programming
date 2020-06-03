#!/usr/bin/python3
"""read_lines function that reads specific lines"""


def read_lines(filename="", nb_lines=0):
    """Reads and prints a specified number of lines"""
    i = 1
    with open('{}'.format(filename)) as f:
        if nb_lines == 0:
            print(f.read(), end="")
        for line in f:
            if i <= nb_lines:
                print(line, end="")
            i += 1
