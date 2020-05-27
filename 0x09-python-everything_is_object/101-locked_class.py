#!/usr/bin/python3
""" class LockedClass with no class or object attribute """


class LockedClass:
    """ prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name
    __slots__ : tell Python not to use a dict, and only allocate space for a
    fixed set of attributes """

    __slots__ = ['first_name']
