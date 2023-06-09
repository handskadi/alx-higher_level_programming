#!/usr/bin/python3
def no_c(my_string):
    # Define a func that removes all chars c and c from str
    rm = ""
    for c in range(len(my_string)):
        if (my_string[c] != 'c' and my_string[c] != 'C'):
            rm += my_string[c]
    return rm
