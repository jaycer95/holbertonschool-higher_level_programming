#!/usr/bin/python3
""" Rectangle class"""


class Rectangle:
    """Define a rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ calculate and return area"""
        return self.__height * self.__width

    def perimeter(self):
        """ calculates and return the perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    def __str__(self):
        pr = ""
        if self.__height == 0 or self.__width == 0:
            return pr
        for i in range(self.__height - 1):
            pr += '#' * self.__width + "\n"
        pr += '#' * self.__width
        return pr
