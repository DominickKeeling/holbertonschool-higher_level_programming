#!/usr/bin/python3
"""
Prints "Prints a square"
"""


def text_indentation(text):
    """
    Checks to make sure size is an int > 0, then prints a square
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    line_breaks = ['.', '?', ':']

    flag = 0
    for i in text:
        if flag == 0:
            if i == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if i in line_breaks:
                print(i)
                print()
                flag = 0
            else:
                print(i, end="")
