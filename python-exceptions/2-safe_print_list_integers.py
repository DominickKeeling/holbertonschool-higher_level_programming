#!/usr/bin/python3
# Write a function that prints the first x elements ofa list and only integers


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except (TypeError, ValueError):
            continue
        else:
            count += 1
    print()
    return count
