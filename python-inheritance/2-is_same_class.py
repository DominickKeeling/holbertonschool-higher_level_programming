#!/usr/bin/python3
"""is_same_class module"""


def is_same_class(obj, a_class):
    """is same class returns true if object is same class and false if not"""

    return type(obj) is a_class
