#!/usr/bin/python3
"""Sendi POST request"""
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    val = {"email": sys.argv[2]}

    data = urllib.parse.urlencode(val).encode("ascii")
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as res:
        print(res.read().decode("utf-8"))
