#!/usr/bin/python3
"""This is the Square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """this is the Square class object of Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        # order matters. follow rectangle
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({%d}) {%d}/{%d} - {%d}".format(self.id,
                                                         self.y,
                                                         self.width)
