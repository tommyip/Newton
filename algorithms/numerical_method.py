"""
Numerical Solutions of Equations
================================
1. Interval Bisection
2. Newton-Raphson method
"""

from mpmath import mpf, fadd, fsub, fmul, fdiv, power
from .helper import *

mp.prec = 32
mp.pretty = True


def interval_bisection(equation, lower, upper) -> str:
    """ Calculate the root of the equation using
    `Interval Bisection` method.

    Examples:
    >>> interval_bisection([1, 0, -3, -4], 2, 3)[0]
    '2.19582335'
    >>> interval_bisection([1, 0, 1, -6], 1, 2)[0]
    '1.63436529'
    >>> interval_bisection([1, 0, 3, -12], 1, 2)[0]
    '1.85888907'
    """

    # Counts the number of iteration
    counter = 0

    equation = mpfiy(equation)
    lower, upper = mpf(lower), mpf(upper)
    index_length = len(equation)
    x = mean(lower, upper)

    previous_alpha = alpha = None
    delta = fsub(upper, lower)

    while delta > power(10, -10) or previous_alpha is None:
        ans = mpf(0)

        # Summing the answer
        for i in range(index_length):
            index_power = index_length - i - 1
            ans = fadd(ans, fmul(equation[i], power(x, index_power)))

        if ans > mpf(0):
            upper = x
        else:
            lower = x

        x = mean(lower, upper)
        previous_alpha, alpha = alpha, x

        if previous_alpha is None:
            continue
        elif previous_alpha == alpha:
            break

        delta = abs(fsub(alpha, previous_alpha))
        counter += 1

    return str(near(alpha, lower, upper)), counter


def newton_raphson_method(equation, approx) -> str:
    """ Calculate the root of the equation using
    `Newton Raphson` method.

    Examples:
    >>> newton_raphson_method([1, 0, -3, -4], 2)[0]
    '2.19582335'
    >>> newton_raphson_method([1, 0, 1, -6], 1)[0]
    '1.63436529'
    >>> newton_raphson_method([1, 0, 3, -12], 1)[0]
    '1.85888907'
    """

    # Counts the number of iteration
    counter = 0

    equation = mpfiy(equation)
    approx, previous_approx = mpf(approx), None
    delta = 100

    while delta > power(10, -8) or previous_approx is None:
        better_approx = fsub(approx, fdiv(
            func(equation, approx),
            func(differentiate(equation), approx)
        ))

        previous_approx, approx = approx, better_approx

        if previous_approx is None:
            continue
        elif previous_approx == approx:
            break

        delta = abs(fsub(approx, previous_approx))
        counter += 1

    return str(approx), counter
