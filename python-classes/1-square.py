#!/usr/bin/python3
# Write a class Square that defines a square by: (based on 0-square.py)
"""This is the Square class"""


class Square:
    """This class defines a square"""

    def __init__(self, size):
        """This method initializes the size of the square"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be greater than or equal to 0")
        self.__size = size
