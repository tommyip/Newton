import sys
sys.path.append('/home/tommy/Documents/project/')
from newton import numerical_method as nm

ans, count = nm.interval_bisection([2, 1, 2, 5, 10], -1000000000, 10000000000, 10)

print(ans, count)
