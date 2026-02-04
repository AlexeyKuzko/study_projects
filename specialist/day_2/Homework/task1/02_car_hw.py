# Автомобиль
# Описать класс Car
class Car:
    def __init__(self, gas=0, capacity=50, gas_per_100km=10):  # У машины должны быть атрибуты и значения по умолчанию
        self.gas = gas  # "сколько бензина в баке" (gas)
        self.capacity = capacity  # "вместимость бака" - сколько максимум влезает бензина (capacity)
        self.gas_per_100km = gas_per_100km  # "расход топлива на 100 км" (gas_per_100km)
        self.mileage = 0  # "пробег" (mileage)

    def fill(self, liters: int | float):  #  метод "залить столько-то литров в бак"
        if self.gas + liters <= self.capacity:  # должна учитываться вместительность бака
            self.gas += liters
            print(f"Залили {liters} литров бензина")
        else:  # если пытаемся залить больше, чем вмещается
            print(f"Бак полон, {self.gas + liters - self.capacity} лишних литров")  # выводим сообщение о лишних литрах
            self.gas = self.capacity  # но бак заполняется полностью

    def ride(self, km: int | float):  # метод "проехать сколько-то км"
        max_km = self.gas / self.gas_per_100km * 100

        if km <= max_km:
            spent = km * self.gas_per_100km / 100
            self.gas -= spent  # в результате поездки потратится бензин
            self.mileage += km  # и увеличится пробег
            print(f"Проехали {km} километров")
        else:  # Если топлива не хватает на указанное расстояние, едем пока хватает топлива.
            self.mileage += max_km
            self.gas = 0
            print(f"Проехали только {max_km} километров — бензин закончился")

    def info(self):
        print(f"Бензина в баке: {self.gas}\nПробег: {self.mileage}")

car1 = Car()
car1.fill(5)  # залили 5 литров
car1.ride(50)  # едем 50 км (если хватит топлива)
car1.info()  # вывести количество бензина в баке и пробег
