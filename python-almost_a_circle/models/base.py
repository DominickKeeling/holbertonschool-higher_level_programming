#!/usr/bin/python3
"""This is the class Base module"""
import json


class Base():
    """This is the Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the json string representation of list_objs to a file"""
        with open((cls.__name__ + ".json"), 'w') as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                jsn = [i.to_dictionary() for i in list_objs]
                jsonfile.write(Base.to_json_string(jsn))

    @staticmethod
    def from_json_string(json_string):
        """Returns a list of the JSON string representation json_string"""
        if (json_string is None or len(json_string) == 0):
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == 'Square':
            dummy_instance = cls(1)
        else:
            dummy_instance = cls(1, 1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        classfile = cls.__name__ + ".json"
        try:
            with open(classfile) as jsn:
                js = Base.from_json_string(jsn.read())
                return [cls.creare(**j) for j in js]
            except IOError:
                return []
