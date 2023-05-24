#!/usr/bin/python3
# write a function with two integers. a and b must be integers or floats
# otherwise raise a TypeError exception with the message 'a must be an integer
# or b must be an integer
# a and b must be first casted to integers if they are float
# Returns an integer: the addition of a and b
# You are not allowed to import any module
"""This is a function that adds 2 integers"""


def add_integer(a, b=98):
    """function for adding integers"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
