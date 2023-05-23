#!/usr/bin/python3
"""This is the Square class"""


class Square:
    """This class defines a square"""

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size == value

    def __init__(self, size=0):
        """This method initializes the square with a size"""
        self.__size = size

    def area(self):
        return self.__size ** 2

    def my_print(self):
        """Public instance method that prints the square with character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
