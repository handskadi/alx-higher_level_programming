#!/usr/bin/python3
""" Pascal's Triangle func """


def pascal_triangle(n):
    """ Represent Pascal's Triangle of size n."""

    if n <= 1:
        my_list = []
        return my_list
    else:
        list_i = [[1]]
        for i in range(n - 1):
            temp = [0] + list_i[-1] + [0]

            row = []

            for j in range(len(list_i[-1]) + 1):
                row.append(temp[j] + temp[j+1])
            list_i.append(row)
        return list_i
