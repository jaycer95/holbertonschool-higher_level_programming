#!/usr/bin/python3
""" create a student class"""


class Student:
    """ defines a student """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list) is False:
            return self.__dict__

        dict = {}
        for strings in attrs:
            if type(strings) is not str:
                return self.__dict__
            if strings in self.__dict__:
                dict[strings] = self.__dict__[strings]
        return dict
