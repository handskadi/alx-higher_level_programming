#!/usr/bin/python3
""" a Text file Reading function """


def read_file(filename=""):
    """ Encoding will be UTF-8
    Print will be to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
