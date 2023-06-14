#!/usr/bin/python3

# Define a func that replaces all occurs of an elm by another in nw list


def search_replace(my_list, search, replace):
    return list(map(lambda e: replace if e == search else e, my_list))
