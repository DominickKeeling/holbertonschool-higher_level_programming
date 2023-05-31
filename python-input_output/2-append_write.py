#!/usr/bin/python3
"""append_write Module"""


def append_write(filename="", text=""):
    """appends a string to the end of file"""

    with open(filename, 'a', encoding="utf+8") as f:
        f.write(text)
        f.close()
        return (len(text))
