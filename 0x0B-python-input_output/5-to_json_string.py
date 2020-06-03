#!/usr/bin/python3
""" define json to string function"""


import json


def to_json_string(my_obj):
    """Return the JSON representation of an object (string)"""

    return json.dumps(my_obj)
