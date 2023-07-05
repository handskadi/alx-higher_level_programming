#!/usr/bin/python3
""" A Real class Rectangle """


class Rectangle:
    """ Represents a recangle """
    def __init__(self, width=0, height=0):
        """ Init a new rectangle """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get of with rectangle's width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get  rectangle's height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Height setter """
        if type(self, value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
