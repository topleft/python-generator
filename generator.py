"""Create a generator gen_seq() that creates the infinite geometric series:
1, 1/2, 1/4, 1/8...

Write a function first_N(num) that sums the first num values

Write a function until_small(epsilon) that sums the sequence until the
additional term is less than some small value epsilon.

"""

import sys
import pytest

def seq_generator():
    """Generates the infinite geometric series 1, 1/2, 1/4, 1/8, ..."""
    i = 1
    while True:
        yield 1.0 / i
        i *= 2

def first_N(num):
    """Use seq_generator() to generate the sum of the first num values of the series."""
    n = 0
    result = 0.0
    seq = seq_generator()
    while n < num:
        result += next(seq)
        n += 1
    return result

def until_small(epsilon):
    """Use seq_generator() to generate the sum of the series until a value smaller
    than epsilon is encountered."""
    current = 1
    result = 0.0
    seq = seq_generator()
    while current > epsilon:
        current = next(seq)
        result += current
    return result

def test_first_N():
    assert 0.0 == first_N(0)
    assert 1.0 == first_N(1)
    assert 1.5 == first_N(2)
    assert 1.75 == first_N(3)
    assert 1.875 == first_N(4)


def test_until_small():
    assert 1.5 == until_small(1.0 / 2)
    assert 1.875 == until_small(1.0 / 8)


def main():
    return pytest.main(__file__)


if __name__ == '__main__':
    sys.exit(main())
