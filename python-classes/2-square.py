#!/usr/bin/python3
# write a class Square that defines a square by:(based on 1-square.py)
"""This is the Square class"""


class Square:
    """This class defines a square"""
    def __init__(self, size=0):
        """This method initializes a square with a size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
