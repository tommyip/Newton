import re
import mpmath as mp
import numpy as np

mp.mp.prec = 32
mp.mp.pretty = True

polynomial_pattern = re.compile('([+|-]?\d*)(x)?(\^\d+)?')


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


def lexer(eq):
    """ Returns a Python list containing the coefficient
    of an equation.

    Example:
    >>> lexer('3x^4 + 5x^3 - x^2 + 8x + 2')
    [3, 5, -1, 8, 2]
    >>> lexer('2x^3 - 5')
    [2, 0, 0, -5]
    >>> lexer('15x^10')
    [15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    """

    matches = re.findall(polynomial_pattern, eq.replace(' ', '').lower())
    matches.pop()
    matches = [list(group) for group in matches]  # Convert tuple-list to multi dimension list

    for group in matches:
        group[-1] = group[-1].replace('^', '')
        if group[0] in ['+', '-']:
            # Add '1' to x without coefficient
            group[0] += '1'
        if group[0] == '':
            group[0] = '1'
        if group[1] == '':
            # Constant
            group[-1] = '0'
        elif group[1] == 'x' and group[-1] == '':
            # Power = 1
            group[-1] = '1'

    matches.sort(key=lambda tup: tup[-1], reverse=True)

    power = int(matches[0][-1])

    coefficient = [0] * (power + 1)

    for group in matches:
        coefficient[power - int(group[-1])] = int(group[0])

    return coefficient
