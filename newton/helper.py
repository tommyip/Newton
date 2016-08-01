"""
Helper functions
====================
1. Get decimal points
1. mean
2. near
3. mpfiy
4. find
"""
import mpmath as mp

mp.mp.prec = 32
mp.mp.pretty = True


def mean(a, b):
    return mp.fdiv(mp.fadd(a, b), mp.mpf(2))


def near(num, a, b):
    if abs(a - num) < abs(b - num):
        return a
    return b


def mpfiy(array):
    return list(map(lambda x: mp.mpf(x), array))
