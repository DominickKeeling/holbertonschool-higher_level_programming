#!/usr/bin/python3
"""This is the Square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """this is the Square class object of Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        # order matters. follow rectangle
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'

    @property
    def size(self):
        """ Getter for size"""
        # remember height, size = width
        return self.width

    @size.setter
    def size(self, size):
        """Setter for size"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """updating the args and the kwargs"""
        if args is not None and len(args) > 0:
            keylist = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, keylist[i], args[i])
        elif kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)
