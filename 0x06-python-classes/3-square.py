#!/usr/bin/python3
""" Creating a Square class """


class Square:
    """ Square class """

    def __init__(self, size=0):
        """ Sets the initial size of the new square object """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """ Calculates the area"""
        return self.__size ** 2
