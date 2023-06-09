#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    # define a func that replaces an item at specific index
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
    return (my_list)
