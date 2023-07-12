#!/usr/bin/python3
""" NyIn class """


class MyInt(int):
    """ MyInt class """
    def __eq__(self, other):
        """Overides & inverts == opr"""
        return int(self) != int(other)

    def __ne__(self, other):
        """Overides & inverts != op"""
        return int(self) == int(other)
