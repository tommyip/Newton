import sys
sys.path.append('/home/tommy/Documents/project/')
from newton import numerical_method as nm

ans = nm.interval_bisection([1, 0, -3, -4], 2, 3, 6)

print(ans)