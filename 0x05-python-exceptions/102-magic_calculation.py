#!/usr/bin/python3
def magic_calculation(a, b):
    my_res = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            my_res += a ** b / i
        except Exception:
            my_res = b + a
            break
    return my_res
