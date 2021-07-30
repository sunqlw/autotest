import pytest


def sum_int(x, y):
    return x+y


def test_print():
    assert sum_int(3, 4) == 6


if __name__ == '__main__':
    pytest.main()