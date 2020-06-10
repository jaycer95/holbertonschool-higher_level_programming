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
