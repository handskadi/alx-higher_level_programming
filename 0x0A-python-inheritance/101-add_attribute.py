#!/usr/bin/python3
""" add attribute mod """


def add_attribute(obj, name, value):
    """ check if att can set & set when possible """
    if hasattr(obj, "__dict__")  or \
        (hasattr(obj, "__slots__") and name in obj.__slots__):
            setattr(obj, name, value)
    else:
         raise TypeError("can't add new attribute")

