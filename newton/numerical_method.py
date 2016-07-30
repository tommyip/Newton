"""
Numerical Solutions of Equations
================================
1. Interval Bisection
2. General iteration method
3. Newton-Raphson method

Each methods would accept an equation, an initial value
and a precision.

Format:
Equation - Array (sort in index order DESC.)
Initial value - Integer
Precision - Integer (number of decimal points)

2x^2 + 4x + 3 = 0
"""
import sys
from mpmath import mpf, mp, mpmathify, fmul, fadd, power
sys.path.append('/home/tommy/Documents/project/')
from newton import helper

mp.prec = 32
mp.pretty = True


def interval_bisection(equation, lower, upper, precision=5):
    """
    Calculate the root of the equation using
    `Interval Bisection` method.
    """

    equation = helper.mpfiy(equation)
    lower, upper = mpf(lower), mpf(upper)
    x = helper.mean(lower, upper)
    index_length = len(equation)

    # previous_alpha = lower
    # current_alpha =

    while helper.decimal_points(x) <= precision:
        ans = mpf(0)
        for index in range(index_length):
            index_power = index_length - index - 1
            ans = fadd(ans, fmul(equation[index], power(x, index_power)))
        if ans > 0:
            upper = x
        else:
            lower = x
        x = helper.mean(lower, upper)

    return mpmathify(helper.near(ans, lower, upper), precision)


def general_iteration_method():
    pass


def newton_raphson_method():
    pass

if __name__ == '__main__':
    interval_bisection([1, -3, 4], 2, 3, 2)
