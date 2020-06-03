#!/usr/bin/python3
""" Define object to dict function """


def class_to_json(obj):
    """ Return dict of obj """

    return obj.__dict__
