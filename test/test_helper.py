import sys
sys.path.append('/home/tommy/Documents/project/')

from newton import helper
from mpmath import mpf, mp

mp.prec = 32
mp.pretty = True


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


def test_number2ordinal():
    assert helper.number2ordinal(1) == '1st'
    assert helper.number2ordinal(2) == '2nd'
    assert helper.number2ordinal(3) == '3rd'
    assert helper.number2ordinal(4) == '4th'
    assert helper.number2ordinal(10652) == '10652nd'

    