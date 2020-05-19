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
    @property
    def size(self):
        """ get size """
        return self.__size
    @size.setter
    def size(self, value):
        """ set the size """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value
    def area(self):
        """ Calculates the area"""
        return self.__size ** 2
    def my_print(self):
        """  prints in stdout the square with the character # """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end="")
            print()
