class Rect:
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    # площадь — пригодится для сравнений
    def area(self):
        return self.length * self.width

    # 1) repr — для разработчика
    def __repr__(self):
        return f"Rect(length={self.length}, width={self.width})"

    # 2) str — для пользователя
    def __str__(self):
        return f"Прямоугольник {self.length} x {self.width}"

    # 3) умножение на число
    def __mul__(self, arg):
        if type(arg) in (int, float):
            return Rect(self.length * arg, self.width * arg)
        else:
            raise TypeError("Multiplier must be int or float")

    # чтобы работало 5 * r1
    def __rmul__(self, arg):
        return self.__mul__(arg)

    # 4) сравнение по площади
    def __lt__(self, other):
        return self.area() < other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()


r1 = Rect(2, 3)
r2 = Rect(4, 5)

print(r1)              # str
print(repr(r1))        # repr

r3 = r1 * 5
print(r3)

print(r1 < r2)
print(r1 == r2)
print(r1 <= r1)
