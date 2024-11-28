print("Pham Viet Quan Mssv 235752021610022")
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return math.pi * self.radius ** 2
    def calculate_circumference(self):
        return 2 * math.pi * self.radius
radius = float(input("Nhập bán kính hình tròn: "))
circle = Circle(radius)
print(f"Diện tích hình tròn là: {circle.calculate_area():.2f}")
print(f"Chu vi hình tròn là: {circle.calculate_circumference():.2f}")
