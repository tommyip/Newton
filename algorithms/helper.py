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
import numpy as np

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


def number2ordinal(num):
    last_char = str(num)[-1]
    if last_char == '1':
        ordinal = 'st'
    elif last_char == '2':
        ordinal = 'nd'
    elif last_char == '3':
        ordinal = 'rd'
    else:
        ordinal = 'th'

    return str(num) + ordinal


def input2int(question='', valid_input=[]):
    error = True

    while error:
        user_input = input(question)
        try:
            output = int(user_input)
            if len(valid_input) > 0:
                if output in valid_input:
                    error = False
            else:
                error = False
        except ValueError:
            print('ERROR: Please enter a valid number.')

    return output


def func(eq, x):
    """ Calculate the answer to f(x) """
    ans, x = mp.mpf(0), mp.mpf(str(x))
    index_length = len(eq)
    for i in range(index_length):
        order = index_length - i - 1
        ans = mp.fadd(ans, mp.fmul(eq[i], mp.power(x, order)))
    return mp.nstr(ans)


def differentiate(eq):
    """
    Eq: 3x^3 + 5x^2 - x + 8
    Return: 9x^2 + 10x - 1
    """
    out = []
    index = len(eq) - 1
    for i in range(index):
        out.append(eq[i] * index)
        index -= 1

    return out