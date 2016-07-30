import sys
sys.path.append('/home/tommy/Documents/project/')

from newton import helper


def test_decimal_points():
    assert helper.decimal_points(1.1) == 1
    assert helper.decimal_points(1.123456) == 6
    assert helper.decimal_points(5) == 0
    assert helper.decimal_points(2.000) == 0
    assert helper.decimal_points(2.654000000000000012345) == 3


def test_mean():
    assert helper.mean(2, 3) == 2.5
    assert helper.mean(5, 5) == 5
    assert helper.mean(0, 22.96) == 11.48
