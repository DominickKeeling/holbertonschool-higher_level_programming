#!/usr/bin/python3
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

    @position
    def position(self):
        return self.__posotion

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2 or \ type(value[0]) is not int or type(value[1]) is not int or \ value[0] < 0 or value[1] < 0:
            raise TypeaError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __init__(self, size=0, position=(0, 0)):
        """This method initializes the square with a size"""
        self.__size = size
        self.__position = position

    def area(self):
        return self.__size ** 2

    def my_print(self):
        """Public instance method that prints the square with character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
