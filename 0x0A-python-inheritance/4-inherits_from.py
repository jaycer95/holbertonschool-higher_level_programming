#!/usr/bin/python3
""" Documentation for inherits-from function """


def inherits_from(obj, a_class):

    """ verifies type of object """

    if issubclass(obj.__class__, a_class) and type(obj) != a_class:
        return True
    return False
