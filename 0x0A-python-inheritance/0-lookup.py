#!/usr/bin/python3
""" Lookup module """


def lookup(obj):
    """list available attributes & methods of an object
    Reurns a list of attr and methods of our object"""
    return dir(obj)
