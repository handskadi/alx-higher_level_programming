#!/usr/bin/python3
""" A file writing function """


def write_file(filename="", text=""):
    """ String to file on UTF-8 """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
