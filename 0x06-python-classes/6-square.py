#!/usr/bin/python3
""" Creating a Square class """


class Square:
    """ Square class """
    def __init__(self, size=0, position=(0, 0)):
        """ Sets the initial size of the new square object """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

        if (type(position) is not tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not (isinstance(position[0], int) or isinstance(position[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0 or len(position) is not 2:
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
        """ get the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """ set the position"""
        if (type(value) is not tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not (isinstance(position[0], int) or isinstance(position[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0 or len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ Calculates the area"""
        return self.__size ** 2

    def my_print(self):
        """  prints in stdout the square with the character # """
        if self.__size == 0:
            print()
        else:
            for lines in range(self.__position[1]):
                print()

            for i in range(self.__size):
                for spaces in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print('#', end="")
                print()
