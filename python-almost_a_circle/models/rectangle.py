#!/usr/bin/python3
"""This is the Rectangle class module"""
from models.base import Base


class Rectangle(Base):
    """This is the Rectangle class object from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if type(value) is not int:
            raise TypeError("Width must be an integer")
        if value <= 0:
            raise ValueError("Width value must be > 0")

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if type(value) is not int:
            raise TypeError("Height must be an integer")
        if value <= 0:
            raise ValueError("Height value must be > 0")
        self.__height = height

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be > 0")
        self.__x = x

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be > 0")
        self.__y = y
