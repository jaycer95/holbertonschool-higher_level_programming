#!/usr/bin/python3
""" Rectangle class"""


class Rectangle:
    """Define a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__class__.number_of_instances += 1
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
            pr += str(self.print_symbol) * self.__width + "\n"
        pr += str(self.print_symbol) * self.__width
        return pr

    def __repr__(self):
        return "Rectangle(%r, %r)" % (self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        self.__class__.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if Rectangle.area(rect_2) > Rectangle.area(rect_1):
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
