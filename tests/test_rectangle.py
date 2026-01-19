import pytest 
import sys
sys.path.append("/home/egor/Python/pytest_introspection/source")
import source.shapes as shapes

def test_area(my_rectangle):
    assert my_rectangle.area() == 10 * 20

def test_perimetr(my_rectangle):
    assert my_rectangle.perimetr() == 2 * (10 + 20)

def test_not_equal(my_rectangle, weird_rectangle):
    assert my_rectangle != weird_rectangle