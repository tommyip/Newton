"""
Numerical Solutions of Equations
================================
1. Interval Bisection
2. General iteration method
3. Newton-Raphson method

Each methods would accept an equation, an initial value
a precision.

Format
-----------------------------------------------
Equation - Array (sort in index order DESC.)
Initial value - Integer
Precision - Integer (number of decimal points)

Example:
-----------------------------------------------
Eq: 2x^2 + 4x + 3 = 0
Equation - [2, 4, 3]
Initial value - 5
Precision - 10
"""

import sys
from mpmath import mpf, mp, fmul, fadd, fsub, power, fneg
sys.path.append('/home/tommy/Documents/project/')
from newton import helper

mp.prec = 32
mp.pretty = True


def interval_bisection(equation, lower, upper, precision=10):
    """
    Calculate the root of the equation using
    `Interval Bisection` method.
    """
    counter = 0
    equation = helper.mpfiy(equation)
    lower, upper = mpf(lower), mpf(upper)
    index_length = len(equation)
    x = helper.mean(lower, upper)

    previous_alpha = alpha = None
    delta = fsub(upper, lower)

    while delta > power(10, fneg(precision)) or previous_alpha is None:
        ans = mpf(0)

        for i in range(index_length):
            index_power = index_length - i - 1
            ans = fadd(ans, fmul(equation[i], power(x, index_power)))

        if ans > mpf(0):
            upper = x
        else:
            lower = x

        x = helper.mean(lower, upper)
        previous_alpha, alpha = alpha, x

        if previous_alpha is None:
            continue
        elif previous_alpha == alpha:
            break
        else:
            delta = abs(fsub(alpha, previous_alpha))
            counter += 1

    return str(helper.near(alpha, lower, upper)), counter


def general_iteration_method():
    pass


def newton_raphson_method():
    pass

if __name__ == '__main__':
    print(interval_bisection([1, 0, -3, -4], 2, 3, 9))
