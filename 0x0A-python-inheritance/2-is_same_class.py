#!/usr/bin/python3
""" function to check class """


def is_same_class(obj, a_class):

    """ verifies class"""

    if type(obj) is a_class:
        return True
    else:
        return False
