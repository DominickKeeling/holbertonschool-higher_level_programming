#!/usr/bin/python3
"""student module"""


class Student:
    """create class called student"""

    def __init__(self, first_name, last_name, age):
        """initializes new student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """turns class to json rep"""

        return self.__dict__
