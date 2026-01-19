import pytest
import sys
sys.path.append("/home/egor/Python/pytest_introspection/source")
import source.shapes as shapes


class TestSquare:
    def setup_method(self):
        self.Square = shapes.Square(5)
    
    def test_area(self):
        assert self.Square.area() == 25

    def test_perimetr(self):
        assert self.Square.perimetr() == 20

    def teardown_method(self):
        del self.Square  # just for studying purpose


### Function-based tests with pytest parametrize decorator ###
@pytest.mark.parametrize("length, expected_area", [
    (3, 9),
    (4, 16),
    (5, 25)
])
def test_square_area(length, expected_area):
    assert shapes.Square(length).area() == expected_area
    
@pytest.mark.parametrize("length, expected_perimetr", [
    (3, 12),
    (4, 16),
    (5, 20)
])
def test_square_perimetr(length, expected_perimetr):
    assert shapes.Square(length).perimetr() == expected_perimetr
