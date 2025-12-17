import pytest

from calculator.core import add, subtract, multiply, divide


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 4) == -8


def test_divide():
    assert divide(6, 3) == 2
    assert divide(7, 2) == 3.5
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        divide(1, 0)