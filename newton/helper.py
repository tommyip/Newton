"""
Helper functions
====================
1. Get decimal points
"""

def decimal_points(x):
    x = round(x, 10)
    split = str(x).strip("0").split('.')
    try:
        floating_points = len(split[1])
        return floating_points
    except IndexError:
        return 0

def mean(a, b):
    return (a + b) / 2