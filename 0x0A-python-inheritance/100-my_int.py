#!/usr/bin/python3
""" Reverse operators """


class MyInt(int):
    """ a class that inherits from int """

    def __init__(self, value):
        self.value = value

    def __eq__(self, x):
        return self.value != x

    def __ne__(self, x):
        return self.value == x
