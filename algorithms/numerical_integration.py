"""
Numerical Integration
=====================
1. Trapezium rule
2. Simpson's rule

Each function
"""

from mpmath import mpf, fadd, fsub, fmul, fdiv, fsub, fsum
from .helper import *

mp.prec = 32
mp.pretty = True


def trapezium_rule(equation: list, lower_bound: int, upper_bound: int, n: int) -> str:
    """ Calculates the area under a curve given
    its equation, lower bound, upper bound and
    number of strips to divide.

    >>> trapezium_rule([1, 0, 0], 0, 2, 100)
    '2.6668'
    >>> trapezium_rule([1, -2, 0, 2], -0.5, 2, 2000.5)
    '3.56645978'
    >>> trapezium_rule([1, -4, 3, 0], 0, 1, 1000)
    '0.416665257'
    """
    width = fdiv(
        abs(fsub(upper_bound, lower_bound)),
        n
    )
    ordinates = list(map(
        lambda x: func(equation, x),
        np.arange(np.float64(lower_bound), np.float64(upper_bound), width)
    ))

    ans = fmul(
        fdiv(width, 2),
        fadd(
            fadd(ordinates[0], ordinates[-1]),
            fmul(2, fsum(ordinates[1:-1]))
        )
    )

    return str(ans)
