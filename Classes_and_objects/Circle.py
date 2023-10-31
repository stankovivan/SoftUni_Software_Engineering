import math
class Circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius


    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_area(self):
        return Circle.pi * math.pow(self.radius, 2)

    def get_circumference(self):
        res = self.radius * 2
        result = res * Circle.pi
        return result


circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())
