#!/usr/bin/python3
""" Base of all Classes  """


class Base:
    """ Base Class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constractor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects