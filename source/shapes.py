import math

class Shape:
    def area(self):
        pass

    def perimetr(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
    def perimetr(self):
        return 2 * math.pi * self.radius
