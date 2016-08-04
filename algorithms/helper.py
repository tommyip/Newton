import mpmath as mp
import numpy as np

mp.mp.prec = 32
mp.mp.pretty = True


def mean(a, b):
    """ Returns the mean of a & b

    Examples:
    >>> mean(2, 3)
    2.5
    >>> mean(5, 5)
    5.0
    >>> mean(0, 22.96)
    11.48
    """
    return mp.fdiv(mp.fadd(a, b), mp.mpf(2))


def near(num, a, b):
    """ Returns the number which is closer to `num`

    Example:
    >>> near(2.2, 2, 3)
    2
    >>> near(1.5, 1, 2)
    2
    >>> near(6, 2, 6)
    6
    """
    if abs(a - num) < abs(b - num):
        return a
    return b


def mpfiy(array):
    """ Converting the type of a list to mpf

    Example:
    >>> mpfiy(range(5))
    [0.0, 1.0, 2.0, 3.0, 4.0]
    """
    return list(map(lambda x: mp.mpf(x), array))


def number2ordinal(num):
    """ Returns the ordinal version of the number.

    Example:
    >>> number2ordinal(1)
    '1st'
    >>> number2ordinal(2)
    '2nd'
    >>> number2ordinal(3)
    '3rd'
    >>> number2ordinal(4)
    '4th'
    >>> number2ordinal(10652)
    '10652nd'
    """
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
    """ Calculate the answer to f(x)

    Example:
    >>> [func([1, 0, -3, -4], i) for i in np.arange(0.0, 5.0, 1)]
    ['-4.0', '-6.0', '-2.0', '14.0', '48.0']
    """
    ans, x = mp.mpf(0), mp.mpf(str(x))
    index_length = len(eq)
    for i in range(index_length):
        order = index_length - i - 1
        ans = mp.fadd(ans, mp.fmul(eq[i], mp.power(x, order)))
    return mp.nstr(ans)


def differentiate(eq):
    """ Returns the derivative of a function.

    Example:
    >>> differentiate([3, 5, -1, 8])
    [9, 10, -1]
    >>> differentiate([9, 10, -1])
    [18, 10]
    >>> differentiate([6, 0, 0, 1, 8, 3, 1, 0])
    [42, 0, 0, 4, 24, 6, 1]
    """
    out = []
    index = len(eq) - 1
    for i in range(index):
        out.append(eq[i] * index)
        index -= 1

    return out