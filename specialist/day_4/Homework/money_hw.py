from functools import total_ordering
import requests
import json

@total_ordering
class Money:
    """Класс для работы с денежными суммами"""
    def __init__(self, rub: int, kop: int):
        """В конструктор можно передать два любых натуральных числа."""
        if rub < 0 or kop < 0:
            raise Exception(f"Ожидаем натуральные числа, были переданы: {rub=}, {kop=}")
        self.total_kopeck = rub * 100 + kop # чтобы проще считать
        self.rub = self.total_kopeck // 100 # рубль 100 копеек
        self.kop = self.total_kopeck % 100 # остаток от целочисленного деления на рубли - копейки

    def __str__(self):
        """Строковое представление суммы"""
        return f"{self.rub}руб {self.kop:02d}коп"

    def __repr__(self):
        """Репрезентация объекта суммы"""
        return f"Money({self.rub}, {self.kop})"

    def __add__(self, other):
        """Операция сложения."""
        return Money(0, self.total_kopeck + other.total_kopeck)

    def __sub__(self, other):
        """Операция вычитания"""
        return Money(0, self.total_kopeck - other.total_kopeck)

    def __mul__(self, number):
        """Умножение на целое число """
        return Money(0, int(self.total_kopeck * number))

    def __eq__(self, other):
        """Сравнение равенства сумм"""
        return self.total_kopeck == other.total_kopeck

    def __lt__(self, other):
        """Сравнение меньше ли"""
        return self.total_kopeck < other.total_kopeck

    def __mod__(self, percent):
        """Вычисление процента от суммы"""
        result = round(self.total_kopeck * percent / 100) # используем округление (функция round())
        return Money(0, result)

    def convert(self, currency: str):
        """Ковертация валют"""
        url = 'https://www.cbr-xml-daily.ru/daily_json.js'
        response = requests.get(url)
        data_dict = json.loads(response.text)
        rate = data_dict["Valute"][currency.upper()]["Value"]
        return round((self.total_kopeck / 100) / rate, 2)

# Создаем сумму из 20 рублей и 120 копеек
money1 = Money(20, 120)  # в конструктор можно передать два любых натуральных числа
# Выводим сумму, с учетом минимального кол-ва копеек <= 99 коп
print(money1) # 21руб 20коп


# Создаем две денежные суммы
money1 = Money(20, 60)
money2 = Money(10, 45)

# Складываем суммы
money3 = money1 + money2
print(money3)  # 31руб 05коп

# Создаем две денежные суммы
money4 = Money(20, 60)
# Находим 20% от суммы
percent_money = money4 % 20
print(percent_money)  # 4руб 12коп

# Конвертация валют
money5 = Money(123, 45)
print(money5.convert("USD"), "$")
print(money5.convert("EUR"), "EUR")
print(money5.convert("GBP"), "GBP")
