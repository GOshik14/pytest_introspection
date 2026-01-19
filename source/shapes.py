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


class Rectangle(Shape):
    def __init__(self, length, width):
        self.lenght = length
        self.width = width

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return self.lenght == other.lenght and\
               self.width == other.width
    
    def area(self):
        return self.lenght * self.width

    def perimetr(self):
        return 2 * (self.lenght + self.width)


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
