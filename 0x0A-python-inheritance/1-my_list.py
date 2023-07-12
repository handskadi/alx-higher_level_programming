#!/usr/bin/python3
""" Sorting List Module """


class MyList(list):
    """ Mylist class that inherts from list class """
    def print_sorted(self):
        """ a sorted list """
        print(sorted(self))
