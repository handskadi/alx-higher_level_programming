#!/usr/bin/python3

# Define a func that returns a key with the biggest integer value


def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    mx_val = 0
    mx_key = None
    for key, value in a_dictionary.items():
        if value > mx_val:
            mx_val = value
            mx_val = key
            return mx_key
