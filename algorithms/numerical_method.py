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
from mpmath import mpf, mp, fmul, fadd, fsub, power, fneg, fdiv
sys.path.append('/home/tommy/Documents/project/')
from newton import helper as hp

mp.prec = 32
mp.pretty = True


def interval_bisection(equation, lower, upper, precision=10):
    """
    Calculate the root of the equation using
    `Interval Bisection` method.
    """
    counter = 0
    equation = hp.mpfiy(equation)
    lower, upper = mpf(lower), mpf(upper)
    index_length = len(equation)
    x = hp.mean(lower, upper)

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

        x = hp.mean(lower, upper)
        previous_alpha, alpha = alpha, x

        if previous_alpha is None:
            continue
        elif previous_alpha == alpha:
            break
        else:
            delta = abs(fsub(alpha, previous_alpha))
            counter += 1

    return str(hp.near(alpha, lower, upper)), counter


def general_iteration_method(equation, approx, precision=8):
    counter = 0
    equation = hp.mpfiy(equation)
    approx = mpf(approx)

    previous_approx = None
    delta = 100
    delta_required = power(10, fneg(precision))

    while delta > delta_required or previous_approx is None:
        previous_approx, approx = approx, hp.func(equation, approx)

        if previous_approx is None:
            continue
        elif previous_approx == approx:
            break
        else:
            delta = abs(fsub(approx, previous_approx))

    return str(approx), counter


def newton_raphson_method(equation, approx, precision=8):
    """
    Calculate the root of the equation using
    `Newton Raphson` method.
    """
    counter = 0
    equation = hp.mpfiy(equation)
    approx = mpf(approx)

    previous_approx = None
    delta = 100
    delta_required = power(10, fneg(precision))

    while delta > delta_required or previous_approx is None:
        better_approx = fsub(approx, fdiv(
            hp.func(equation, approx),
            hp.func(hp.differentiate(equation), approx)
        ))

        previous_approx, approx = approx, better_approx

        if previous_approx is None:
            continue
        elif previous_approx == approx:
            break
        else:
            delta = abs(fsub(approx, previous_approx))
            counter += 1

    return str(approx), counter

if __name__ == '__main__':
    # print(interval_bisection([1, 0, -3, -4], 2, 3, 9))
    print(general_iteration_method([2, 0, -2], 2, 7))
    # print(newton_raphson_method([1, 0, -3, -4], 2, 8))
