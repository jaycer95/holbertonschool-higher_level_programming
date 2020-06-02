#!/usr/bin/python3
""" Documentation for is kind of class function """


def is_kind_of_class(obj, a_class):
    """ verify object type """

    if isinstance(obj, a_class):
        return True
    return  False
