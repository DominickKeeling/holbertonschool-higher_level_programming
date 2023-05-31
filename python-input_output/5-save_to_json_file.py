#!/usr/bin/python3
"""save to json module"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file in json"""
    with open(filename, 'w', encoding="utf+8") as f:
        json.dump(my_obj, f)
