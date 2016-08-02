import sys
import numpy as np
sys.path.append('/home/tommy/Documents/project/')

from newton import helper as hp
from mpmath import mpf, mp

mp.prec = 32
mp.pretty = True


def test_mean():
    assert hp.mean(2, 3) == 2.5
    assert hp.mean(5, 5) == 5
    assert hp.mean(0, 22.96) == mpf('11.48')


def test_near():
    assert hp.near(2.2, 2, 3) == 2
    assert hp.near(1.5, 1, 2) == 2
    assert hp.near(6, 2, 6) == 6


def test_mpfiy():
    assert hp.mpfiy(range(5)) == [mpf('0.0'), mpf('1.0'),
                                      mpf('2.0'), mpf('3.0'), mpf('4.0')]


def test_number2ordinal():
    assert hp.number2ordinal(1) == '1st'
    assert hp.number2ordinal(2) == '2nd'
    assert hp.number2ordinal(3) == '3rd'
    assert hp.number2ordinal(4) == '4th'
    assert hp.number2ordinal(10652) == '10652nd'


def test_func():
    assert [hp.func([1, 0, -3, -4], i) for i in np.arange(0.0, 10.0, 1)] \
            == list(map(lambda x: str(x), [-4.0, -6.0, -2.0, 14.0, 48.0,
                106.0, 194.0, 318.0, 484.0, 698.0]))
    assert [hp.func([2, -6, 0, 0, 2], i) for i in np.arange(2.0, 3.0, 0.1)] \
            == list(map(lambda x: str(x), [-14.0, -14.6698, -15.0368, -15.0338, -14.5888, -13.625,
                -12.0608, -9.8098, -6.7808, -2.8778]))

