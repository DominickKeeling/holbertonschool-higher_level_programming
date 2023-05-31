#!/usr/bin/python3
"""read_file module"""


def read_file(filename=""):
    """read file opens a file and prints to STDOUT"""

    with open(filename, encoding="utf+8") as f:
        print(f.read(), end="")
        f.close()
