import sys
sys.path.append('/home/tommy/Documents/project/')
from newton import numerical_method as nm
import mpmath


def test_interval_bisection():
    assert nm.interval_bisection([1, 0, -3, -4], 2, 3, 11) == 2.19582335
