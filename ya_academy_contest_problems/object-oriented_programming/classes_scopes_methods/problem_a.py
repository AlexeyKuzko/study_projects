"""Solution for Yandex Academy Python Handbook contest solutions: Object Oriented Programming / Classes Scopes Methods / problem A."""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
