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
sys.path.append('/home/tommy/Documents/project/')
from newton import helper


def interval_bisection(equation, lower, upper, precision=5):
    """
    Calcuate the root of the equation using 
    `Interval Bisection` method.
    """
    ans = 0
    x = helper.mean(lower, upper)
    while helper.decimal_points(x) <= precision:
        for index in range(len(equation)):
            power = len(equation) - index - 1
            ans += equation[index] * (x * power)


def general_iteration_method():
    pass


def newton_raphson_method():
    pass
