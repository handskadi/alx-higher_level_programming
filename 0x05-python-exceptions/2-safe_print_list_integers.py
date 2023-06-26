#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    tracker = 0
    for index in range(x):
        try:
            print("{:d}".format(my_listy[index]), end="")
            tracker = tracker + 1
        except TypeError:
            pass
        except ValueError:
            pass
    print("")
    return tracker
