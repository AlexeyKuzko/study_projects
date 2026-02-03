import math


class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def distance(self, other_point) -> float:
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


# пример работы метода
# p1 = Point(4, 4, "red")
# p2 = Point(3, 3, "green")

# result = p1.distance(p2)
# print(result)


# Дан список точек нарисованных красным(red) и зеленым(green) цветами
# Точно известно, что точек каждого цвета ровно три,
# но порядок точек в списке произвольный
points = [
    Point(2, 7, "red"),
    Point(12, 7, "green"),
    Point(5, -2, "red"),
    Point(4, 8, "green"),
    Point(10, -2, "green"),
    Point(-12, 0, "red")
]
# Все точки одного цвета соединены линиями и образуют треугольник

# Задание-1: доработайте конструктор class Point для хранения цвета точки
# Задание-2: реализуйте метод distance()
# Задание-3: вычислите площади треугольников образованных из точек одного цвета(зеленый и красный)
# для вычисления площади можно использовать формулу Герона:
# math.sqrt(p * (p-a) * (p-b) * (p-c)), где p - это полупериметр

area = {}
for color in ("red", "green"):
    same_color_points = []
    for point in points:
        if point.color == color:
            same_color_points.append(point)
    a = same_color_points[0].distance(same_color_points[1])
    b = same_color_points[1].distance(same_color_points[2])
    c = same_color_points[2].distance(same_color_points[0])
    p = (a + b + c) / 2
    area[color] = math.sqrt(p * (p-a) * (p-b) * (p-c))

red_area = area["red"]
green_area = area["green"]

print("Площадь красного треугольника = ", red_area)
print("Площадь зеленого треугольника = ", green_area)
