#!/usr/bin/python3
def multiple_returns(x):
    my_tuple = ()
    if len(x) == 0:
        my_tuple = 0, "None"
    else:
        my_tuple = len(x), x[0]
    return my_tuple
