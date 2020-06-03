#!/usr/bin/python3
""" define save to json file fct """


import json
import sys


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON representation """

    with open(filename, 'w') as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    """creates an Object from a JSON file"""

    with open(filename) as f:
        return json.load(f)

filename = "add_item.json"

try:
    list = load_from_json_file(filename)
except Exception:
    list = []

for i in range(1, len(sys.argv)):
    list.append(sys.argv[i])

save_to_json_file(list, filename)
