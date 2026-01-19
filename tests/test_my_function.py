import pytest
import sys
sys.path.append("/home/egor/Python/pytest_introspection/source")
import source.my_functions as my_funcs


### Simple math tests ###

def test_add_positive():
    assert my_funcs.add(1, 2) == 3

def test_add_negative():
    assert my_funcs.add(-1, -2) == -3

def test_add_both_neg_pos():
    assert my_funcs.add(1, -2) == -1


def test_divide_positive():
    assert my_funcs.divide(4, 2) == 2

def test_divide_negative():
    assert my_funcs.divide(-4, -2) == 2

def test_divide_both_neg_pos():
    assert my_funcs.divide(-4, 2) == -2
