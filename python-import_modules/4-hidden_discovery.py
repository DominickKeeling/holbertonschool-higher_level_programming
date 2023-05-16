#!/usr/bin/python3
# write a program that prints all the names defined by the compiled
# module hidden_4.pyc

if __name__ == "__main__":
    import hidden_4
    for i in dir(hidden_4):
        if i[0] != "_":
            print(i)
