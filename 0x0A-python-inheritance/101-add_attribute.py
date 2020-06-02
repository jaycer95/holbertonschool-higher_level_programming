#!/usr/bin/python3
""" add attribute function """


def add_attribute(obj, attribute, value):
    """ adds a new attribute to an object if its possible
    else raise exception"""

    if hasattr(obj, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
