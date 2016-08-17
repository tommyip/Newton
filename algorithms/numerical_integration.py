"""
Numerical Integration
=====================
1. Trapezium rule
2. Simpson's rule
"""

from mpmath import fadd, fsub, fmul, fdiv, fsum
from .helper import *

mp.prec = 32
mp.pretty = True


def trapezium_rule(equation, lower_bound, upper_bound, n) -> str:
    """ Given an equation, lower bound, upper bound and
    number of strips, returns the area under a curve by
    dividing the area into n trapezium and summing the
    individual area.

    >>> trapezium_rule([1, 0, 0], 0, 2, 100)
    '2.6668'
    >>> trapezium_rule([1, -2, 0, 2], -0.5, 2, 2000.5)
    '3.56645978'
    >>> trapezium_rule([1, -4, 3, 0], 0, 1, 1000)
    '0.416665257'
    """

    # Divide the total width by the number of division to get the width of each trapezium
    trapezium_width = fdiv(
        abs(fsub(upper_bound, lower_bound)), n
    )

    # Tabulates the temporary results by mapping each y to f(x)
    ordinates_table = list(map(
        lambda x: func(equation, x),
        np.arange(
            np.float64(lower_bound),
            np.float64(upper_bound),
            trapezium_width
        )
    ))

    ans = fmul(
        fdiv(trapezium_width, 2),
        fadd(
            # Sum of the first and last ordinates
            fadd(ordinates_table[0], ordinates_table[-1]),
            fmul(2,
                 # Sum of the remaining ordinates
                 fsum(ordinates_table[1:-1]))
        )
    )

    return str(abs(ans))


def simpson_rule(equation, lower_bound, upper_bound, n) -> str:
    """ Given an equation, lower bound, upper bound and
    number of strips, returns the area under a curve by
    dividing the area into even number of parallel strips
    n, and approximates the area of pairs of strips using
    parabolas.

    >>> trapezium_rule([1, 0, 0], 0, 2, 100)
    '2.6668'
    >>> trapezium_rule([1, -2, 0, 2], -0.5, 2, 2000.5)
    '3.56645978'
    >>> trapezium_rule([1, -4, 3, 0], 0, 1, 1000)
    '0.416665257'
    """
    pass
