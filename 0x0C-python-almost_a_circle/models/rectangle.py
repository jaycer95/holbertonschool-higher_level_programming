#!/usr/bin/python3
""" write the class Rectangle that inherits from Base """


from models.base import Base


class Rectangle(Base):
    """ Class Rectangle inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ init """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width"""

        return self.__width

    @width.setter
    def width(self, value):
        """ width conditions """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ height """

        return self.__height

    @height.setter
    def height(self, value):
        """ height conditions """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ x """

        return self.__x

    @x.setter
    def x(self, value):
        """ x conditions """

        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ y """

        return self.__y

    @y.setter
    def y(self, value):
        """ y conditions """

        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ area """

        return self.__height * self.__width

    def display(self):
        """ display """

        for k in range(self.__y):
            print()
        for i in range(self.__height):
            for l in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ str """

        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                                                self.x, self.y, self.width,
                                                self.height)

    def update(self, *args, **kwargs):
        """ update """

        for i, arg in enumerate(args):
            if i == 0:
                self.id = arg
            if i == 1:
                self.width = arg
            if i == 2:
                self.height = arg
            if i == 3:
                self.x = arg
            if i == 4:
                self.y = arg

        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            if key == "width":
                self.width = value
            if key == "height":
                self.height = value
            if key == "x":
                self.x = value
            if key == "y":
                self.y = value

    def to_dictionary(self):
        """dictionary"""
        dict1 = {'x': self.x, 'y': self.y, 'id': self.id,
                 'height': self.height, 'width': self.width}
        return dict1
