#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    # integers representing the Pascal's triangle
    list = []
    for i in range(n):
        temp_list = []
        for j in range(i+1):
            if j == 0 or j == i:
                temp_list.append(1)
            else:
                temp_list.append(list[i-1][j-1] + list[i-1][j])
        list.append(temp_list)
    return list
