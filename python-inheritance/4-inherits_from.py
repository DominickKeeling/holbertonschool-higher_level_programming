#!/usr/bin/python3
"""inherits_from module"""


def inherits_from(obj, a_class):
    """ function that returns True if the object is an instance of a class"""

    return type(obj) != a_class and isinstance(obj, a_class)
