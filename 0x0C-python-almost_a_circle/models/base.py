#!/usr/bin/python3
""" This class will be the base of all other classes in this project """


import json
import os.path


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
        filename = str(cls.__name__) + ".json"
        if list_objs is not None:
            for i in list_objs:
                lists.append(cls.to_dictionary(i))
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(lists))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""

        if not json_string or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""

        if cls.__name__ == 'Rectangle':
            dummy = cls(7, 14)
        if cls.__name__ == 'Square':
            dummy = cls(5)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances"""
        filename = cls.__name__ + ".json"
        lists = []
        if os.path.isfile(filename):
            with open(filename) as f:
                for line in f:
                    text = cls.from_json_string(line)
                    for i in text:
                        lists.append(cls.create(**i))
            return lists
