#!/usr/bin/python3
""" Inhertis From Module"""


def inherits_from(obj, a_class):
    """ Checks if it inhertis from Module """
    return isinstance(obj, a_class) and type(obj) != a_class
