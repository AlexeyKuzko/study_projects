"""Класс Rect с демонстрацией работы магических методов"""

class Rect:
    """Класс прямоугольника"""
    def __init__(self, length=1.2, width=3):  # пре
        """Конструктор с присвоением атрибутов класса - длины и ширины"""
        self.length = length
        self.width = width
    # задания на magic methods: 1) __repr__() 2) __str__()
    def __repr__(self):
        """Метод возвращает точное строковое представление объекта (для разработчика)"""
        return f"Rect({self.length=}, {self.width=})"

    def __str__(self):
        """Метод возвращает удобное строковое представление объекта (для пользователя)"""
        return f"Прямоугольник: длина {self.length} и ширина {self.width}"

    # 3) умножение на число методом __mul__
    def __mul__(self, arg):
        """Метод увеличивает прямоугольник в arg раз"""
        if type(arg) in (int, float):
            return Rect(self.length * arg, self.width * arg)
        else:
            raise TypeError("Тип аргумента метода __mul__ должен быть int или float")

    # 4) сравнения прямоугольников по площади
    def area(self):
        """Метод возвращает площадь прямоугольника, можно использовать для дальнейших сравнений"""
        return self.length * self.width

    def __lt__(self, other):
        """Меньше ли площадь прямоугольника, чем у other прямоугольника"""
        return self.area() < other.area()

    def __gt__(self, other):
        """Больше ли площадь прямоугольника, чем у other прямоугольника"""
        return self.area() > other.area()

    def __le__(self, other):
        """'Меньше или равна' площадь прямоугольника, чем у other прямоугольника"""
        return self.area() <= other.area()

    def __ge__(self, other):
        """'Больше или равна' площадь прямоугольника, чем у other прямоугольника"""
        return self.area() >= other.area()

    def __eq__(self, other):
        """Равна ли площадь прямоугольника площади other прямоугольника"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Не равна ли площадь прямоугольника площади other прямоугольника"""
        return self.area() != other.area()


r1 = Rect()
r2 = Rect(4, 5.67)
r3, r4 = r1 * 5, r2 * 0.42   # mul

print(f"Даны прямоугольники (экземпляры): "
      f"\n{r1} ({repr(r1)})\n{r2} ({repr(r2)})\n{r3} ({repr(r3)})\n{r4} ({repr(r4)})")  # str и repr

# сравнения, которым тоже можно написать f-стринги с объяснением, что с чем сравниваем
print(r1 < r2)  # lt
print(r3 > r4)  # gt
print((r1 <= r4) is True) # le (решил немного поиграться)
print(not r2 >= r3) # ge (пусть везде будет True для красоты)
print((r4 == r2) is False)  # eq
print((r3 != r3) != True)  # ne
