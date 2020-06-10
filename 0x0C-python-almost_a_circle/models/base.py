#!/usr/bin/python3
""" This class will be the base of all other classes in this project """


import json


class Base:
    """ manage id attribute in all your future classes
    and to avoid duplicating the same code """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """

        if list_dictionaries is None or (len(list_dictionaries) == 0):
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""

        lists = []
        filename = cls.__name__ + ".json"
        if lists is not None:
            for i in list_objs:
                lists.append(cls.to_dictionary(i))
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(lists))
