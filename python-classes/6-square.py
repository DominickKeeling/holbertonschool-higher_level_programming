#!/usr/bin/python3
"""This is the Square class"""


class Square:
    """This class defines a Square"""
   def __init__(self, size=0, position=(0,0)):
       self.size = size
       self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size == value

    @property
    def position(self):
        """Getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2 or \ type(value[0]) is not int or type(value[1]) is not int or \ value[0] < 0 or value[1] < 0:
            raise TypeaError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        """Public instance method that prints the square with character #"""
        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
