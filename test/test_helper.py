import sys
sys.path.append('/home/tommy/Documents/project/')

from newton import helper
from mpmath import mpf, mp

mp.prec = 32
mp.pretty = True


def test_decimal_points():
    assert helper.decimal_points(1.1) == 1
    assert helper.decimal_points(1.123456) == 6
    assert helper.decimal_points(5) == 0
    assert helper.decimal_points(2.000) == 0
    assert helper.decimal_points(2.654000000000000012345) == 3
    assert helper.decimal_points(mpf(2.6535)) == 4


def test_mean():
    assert helper.mean(2, 3) == 2.5
    assert helper.mean(5, 5) == 5
    assert helper.mean(0, 22.96) == mpf('11.48')


def test_near():
    assert helper.near(2.2, 2, 3) == 2
    assert helper.near(1.5, 1, 2) == 2
    assert helper.near(6, 2, 6) == 6


def test_mpfiy():
    assert helper.mpfiy(range(5)) == [mpf('0.0'), mpf('1.0'),
                                      mpf('2.0'), mpf('3.0'), mpf('4.0')]


def test_find_precision():
    assert helper.find_precision(mpf('0.0001')) == 3
    assert helper.find_precision(mpf('0.0056789')) == 2
    # assert helper.find_precision(mpf('0.00004325')) == 4
