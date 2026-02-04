"""Автомобиль"""
class Car:
    """
    Класс Car — модель автомобиля.

    Атрибуты:
    - gas: сколько бензина в баке
    - capacity: вместимость бака (максимум бензина)
    - gas_per_100km: расход топлива на 100 км
    - mileage: пробег
    """

    def __init__(self, gas=0, capacity=50, gas_per_100km=10):
        """
        Создаёт объект автомобиля с начальными параметрами.

        Параметры:
        - gas: начальное количество бензина в баке
        - capacity: вместимость бака
        - gas_per_100km: расход топлива на 100 км
        """
        self.gas = gas
        self.capacity = capacity
        self.gas_per_100km = gas_per_100km
        self.mileage = 0

    def fill(self, liters: int | float):
        """
        Метод «залить столько-то литров в бак».

        Учитывает вместимость бака:
        - если бензин помещается, он добавляется в бак;
        - если нет — бак заполняется полностью, а лишние литры выводятся в сообщении.
        """
        if self.gas + liters <= self.capacity:
            self.gas += liters
            print(f"Залили {liters} литров бензина")
        else:
            print(f"Бак полон, {self.gas + liters - self.capacity} лишних литров")
            self.gas = self.capacity

    def ride(self, km: int | float):
        """
        Метод «проехать указанное количество километров».

        Во время поездки:
        - уменьшается количество бензина;
        - увеличивается пробег.

        Если топлива не хватает на заданное расстояние,
        машина едет, пока хватает топлива.
        """
        max_km = self.gas / self.gas_per_100km * 100

        if km <= max_km:
            spent = km * self.gas_per_100km / 100
            self.gas -= spent
            self.mileage += km
            print(f"Проехали {km} километров")
        else:
            self.mileage += max_km
            self.gas = 0
            print(f"Проехали только {max_km} километров — бензин закончился")

    def info(self):
        """
        Выводит информацию о текущем состоянии автомобиля:
        - сколько бензина в баке;
        - какой пробег.
        """
        print(f"Бензина в баке: {self.gas}\nПробег: {self.mileage}")

car1 = Car()  # создали экземпляр автомобиля
car1.fill(5)  # залили 5 литров
car1.ride(50)  # едем 50 км (если хватит топлива)
car1.info()  # вывести количество бензина в баке и пробег
