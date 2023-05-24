#!/usr/bin/python3
"""
Prints "My name is First_name, Last_name"
"""


def say_my_name(first_name, last_name=""):
    """ Checks to make sure both passed variables is a string """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
