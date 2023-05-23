#!/usr/bin/python3
# write a square that defines a square by:(based on 2-square.py)
"""This is the Square class"""


class Square:
    """This class defines the square"""
    def __init__(self, size=0):
        """This initializes the square size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size ** 2
