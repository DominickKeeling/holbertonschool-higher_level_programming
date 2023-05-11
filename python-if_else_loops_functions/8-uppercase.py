#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        ascii_val = ord(str[i])
        if 97 <= ascii_val <= 122:
            ascii_val -= 32
        print("{}".format(chr(ascii_val)), end="")
    print()
