#!/usr/bin/python3
"""student module"""


class Student:
    """create class called student"""

    def __init__(self, first_name, last_name, age):
        """initializes new student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves dictionary"""

        if attrs is None or type(attrs) is not list:
            return self.__dict__
        else:
            dict1 = {}
            for i in attrs:
                if type(i) != str:
                    return self.__dict__
                if i in self.__dict__.keys():
                    dict1[i] = self.__dict__[i]
            return dict1

    def reload_from_json(self, json):
        """return json rep of objects"""

        for i in json.keys():
            self.__dict__.update(json)
