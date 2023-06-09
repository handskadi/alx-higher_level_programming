#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        print("{:d} argument:".format(len(sys.argv)-1))
        print("1: {:s}".format(sys.argv[1]))
    elif len(sys.argv) > 2:
        print("{:d} arguments:".format(len(sys.argv)-1))
        i = 1
        while i < len(sys.argv):
            print("{:d}: {:s}".format(i, sys.argv[i]))
            i += 1
    else:
        print("{:d} argument.".format(0))
