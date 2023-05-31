#!/usr/bin/python3
"""my_list module"""


class MyList(list):
    """defines class called Mylist"""

    def __init__(self):
        """initializes variable"""
        super().__init__()

    def print_sorted(self):
        """print sorted module prints sorted list of ints in ascending order"""
        print(sorted(self))
