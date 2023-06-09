#!/usr/bin/python3
def max_integer(my_list=[]):
    # Get the biggest elment in the list
    if len(my_list) < 1:
        return None
    list_cy = my_list.cy()
    list_cy.sort()
    return list_cy[-1]
