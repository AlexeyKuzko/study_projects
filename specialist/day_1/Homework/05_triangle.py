from typing import Self


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other_point: Self) -> float:
        pass


class Triangle:
    def __init__(self, p1: Point, p2: Point, p3: Point):
        pass

    def perimeter(self):
        pass

    def area(self):
        # Для нахождения площади, используйте формулу Герона
        pass


# Треугольник задан координатами трех точек
triangle = Triangle(Point(2, 4), Point(6, 8), Point(8, 0))

# Задание: 
# найдите площадь и периметр треугольника, реализовав методы area() и perimeter()

print("Периметр треугольника = ", triangle.perimeter())
print("Площадь треугольника = ", triangle.area())
