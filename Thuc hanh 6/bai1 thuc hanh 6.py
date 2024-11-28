print("Pham Viet Quan Mssv 235752021610022")
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2
circle = Circle(2)
print("Diện tích hình tròn là:", circle.calculate_area())
