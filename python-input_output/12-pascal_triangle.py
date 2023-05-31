#!/usr/bin/python3
"""Technical interview preparation:
Create a function def pascal_triangle(n):
that returns a list of list"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal’s triangle of n"""
    if n <= 0:
        return []
    pascal = [[1]]
    for i in range(1, n):
        row = [1]
        prev = pascal[i - 1]
        for j in range(len(prev)):
            if j + 1 < len(prev):
                row.append(prev[j] + prev[j + 1])
        row.append(1)
        pascal.append(row)
    return pascal
