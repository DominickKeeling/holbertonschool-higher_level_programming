#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    n = a_dictionary.copy()
    for x in n:
        n[x] = n[x] * 2
    return n
