#!/usr/bin/python3
def uniq_add(my_list=[]):
    e = 0
    for t in set(my_list):
        e += t
    return e
