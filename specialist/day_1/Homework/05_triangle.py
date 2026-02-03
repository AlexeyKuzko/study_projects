from typing import Self


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other_point: Self) -> float:
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


class Triangle:
    def __init__(self, p1: Point, p2: Point, p3: Point):
        self.p1, self.p2, self.p3 = p1, p2, p3

    @property
    def sides(self):
        return (self.p1.distance(self.p2), self.p2.distance(self.p3), self.p3.distance(self.p1))

    def perimeter(self):
        a, b, c = self.sides
        return a + b + c

    def area(self):
        a, b, c = self.sides
        p = self.perimeter() / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5


# Треугольник задан координатами трех точек
triangle = Triangle(Point(2, 4), Point(6, 8), Point(8, 0))

# Задание: 
# найдите площадь и периметр треугольника, реализовав методы area() и perimeter()

print("Периметр треугольника = ", triangle.perimeter())
print("Площадь треугольника = ", triangle.area())
