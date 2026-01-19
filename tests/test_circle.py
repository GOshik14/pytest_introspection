import pytest
import math
import sys
sys.path.append("/home/egor/Python/pytest_introspection/source")
import source.shapes as shapes

class TestCircle:

    def setup_method(self, method):
        print(f"Setting up {method}")
        circle = shapes.Circle(3)
        self.circle = circle

    def test_radius_one(self):
        self.circle.radius = 1
        print(f"Circle's radius(it've changed to 1) equals to {self.circle.radius}")
        assert self.circle.radius == 1


    def test_radius_two(self):
        print(f"Circle's radius(By default equals 3,"
              f"but it've changed to 1 in time of previous method call)"
              f"equals to {self.circle.radius}")
        assert self.circle.radius == 3

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2
    
    def test_perimetr(self):
        assert self.circle.perimetr() == 2 * self.circle.radius * math.pi

    def teardown_method(self, method):
        print(f"Tearing down {method}")
        del self.circle
    
    def test_not_same_area_rectangle(self, my_rectangle):
        assert self.circle.area() != my_rectangle.area()
