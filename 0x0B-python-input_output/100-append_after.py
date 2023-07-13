#!/usr/bin/python3
""" Append Mod """


def append_after(filename="", search_string="", new_string=""):
    """ Append fun """

    stringme = ""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            stringme += line
            if search_string in line:
                stringme += new_strin
    with open(filename, mode="w") as f:
        f.write(stringme)
