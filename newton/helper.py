"""
Helper functions
====================
1. Get decimal points
"""
import mpmath as mp

mp.mp.prec = 32
mp.mp.pretty = True


def decimal_points(x):
    x = mp.mpmathify(x)
    split = str(x).strip("0").split('.')
    try:
        floating_points = len(split[1])
        return floating_points
    except IndexError:
        return 0


def mean(a, b):
    return mp.fdiv(mp.fadd(a, b), mp.mpf(2))


def near(num, a, b):
    if abs(a - num) < abs(b - num):
        return a
    return b


def mpfiy(array):
    return list(map(lambda x: mp.mpf(x), array))


def find_precision(num):
    precision = 0
    decimal_part = mp.nstr(num).split('.')[1]
    for i in range(len(decimal_part)):
        if decimal_part[i] == '0':
            precision += 1
        else:
            break
    return precision
