#!/usr/bin/python3
""" Rectangle Mod """
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle CLass """
    def __init__(self, width, height):
        """ initiate rect method """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
