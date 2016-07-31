import sys
sys.path.append('/home/tommy/Documents/project/')
from newton import numerical_method as nm

ans, count = nm.interval_bisection([1, 3, -4, 0, 2, 0, 8], -100000, -1000, 12)

print(ans, count)
