#!/usr/bin/python3

# Define a func that returns a list with all values * num (no loop)


def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))
