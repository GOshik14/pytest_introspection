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
