#!/usr/bin/python3
for c in reversed(range(97, 123)):
    print("{:c}".format(c if (ch % 2 == 0) else (ch - 32)), end='')
