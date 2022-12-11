import pytest

from src.assignment_1_2 import *

def test_divide():
    result = divide(11, 4)
    assert result == 2.75

    result = divide(11, 4, "floor_division")
    assert result == 2

    result = divide(11, 4, "modulus")
    assert result == 3
