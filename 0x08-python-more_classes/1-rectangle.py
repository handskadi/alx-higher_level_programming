#!/usr/bin/python3
""" A Real class Rectangle """


class Rectangle:
    """ Represents a recangle """

    def __init__(self, width, height):
        """ Init a new rectangle """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Get of with rectangle's width"""
        return self.height = height

    @width.setter
    def width(self, value):
        if not instance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
