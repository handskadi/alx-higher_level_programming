#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        my_result = fct(*args)
    except Exception as ex:
        sys.stderr.write("Exception: {}\n".format(ex))
        my_result = None
    return (my_result)
