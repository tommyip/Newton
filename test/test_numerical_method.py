import sys
sys.path.append('/home/tommy/Documents/project/')
from newton import numerical_method as nm


def test_interval_bisection():
    assert nm.interval_bisection([1, 0, -3, -4], 2, 3, 10)[0] == '2.19582335'
    assert nm.interval_bisection([1, 0, 1, -6], 1, 2, 10)[0] == '1.63436529'
    assert nm.interval_bisection([1, 0, 3, -12], 1, 2, 10)[0] == '1.85888907'
