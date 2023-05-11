#!/usr/bin/python3
# write  a program that imports the function def add(a, b): from the file
# add_0.py and prints the result of the addition 1 + 2 = 3
from add_0 import add

__name__ == '__main__'
a = 1
b = 2
result = add(a, b)
print("{} + {} = {}".format(a, b, result))
