#!/usr/bin/python3
"""Write the class Square that inherits from Rectangle """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ init """

        super().__init__(size, size, x, y, id)
        self.size = size
        self.x = x
        self.y = y

    def __str__(self):
        """ str """

        return "[{}] ({}) {}/{} - {}".format(type(self).__name__, self.id,
                                             self.x, self.y, self.size)

    @property
    def size(self):
        """size getter"""

        return self.width

    @size.setter
    def size(self, value):
        """ size """

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update """

        for i, arg in enumerate(args):
            if i == 0:
                self.id = arg
            if i == 1:
                self.size = arg
            if i == 2:
                self.x = arg
            if i == 3:
                self.y = arg

        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            if key == "size":
                self.size = value
            if key == "x":
                self.x = value
            if key == "y":
                self.y = value
