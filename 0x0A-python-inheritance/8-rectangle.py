#!/usr/bin/python3
""" Create class """
BaseGeometry = __import__("7-basegeometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class
    inherits from BaseGeometry class """

    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height
