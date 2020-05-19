#!/usr/bin/python3
""" Creating a Square class """
class Square:
    """ Square class """
    def __init__(self, size = 0, position = (0, 0)):
        """ Sets the initial size of the new square object """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

        if type(position) is not tuple or
        all(isinstance(n, int) for n in position) == false or
        position[0] < 0 or position[1] < 0 or len(position) != 2
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position
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
    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, value):
        if type(value) is not tuple or
        all(isinstance(n, int) for n in value) == false or
        value[0] < 0 or value[1] < 0 or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive int\
egers")
        else:
            self.__position = value
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
