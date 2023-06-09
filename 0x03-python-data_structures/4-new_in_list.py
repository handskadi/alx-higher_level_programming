#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    #Alter element in copy list
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)
    cy = [x for x in my_list]
    cy[idx] = element
    return (cy)
