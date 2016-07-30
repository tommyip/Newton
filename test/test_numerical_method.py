import sys
sys.path.append('/home/tommy/Documents/project/')
from newton import numerical_method as nm


def test_interval_bisection():
    assert nm.interval_bisection([1, 0, -3, -4], 2, 3, 6) == 2.1875

