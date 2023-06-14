#!/usr/bin/python3

# Define a func that returns a new dictionary with all values muoltiplied by two


def multiply_by_2(a_dictionary):
    multiplied_dict = {}
    for key, value in a_dictionary.items():
        multiplied_dict[key] = value * 2
    return multiplied_dict
