#!/usr/bin/python3
""" Documentation for add_niteger function """


def add_integer(a, b=98):
    """ Returns the sum of two integers or floats
    """

    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    elif not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    elif isinstance(a, float):
        a = int(a)
    elif isinstance(b, float):
        b = int(b)

    return a + b
