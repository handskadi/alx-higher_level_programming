#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        numb = 0
        dm = 0
        for tup in my_list:
            numb += (tup[0] * tup[1])
            dm += tup[1]
        return (numb / dm)
    return 0
