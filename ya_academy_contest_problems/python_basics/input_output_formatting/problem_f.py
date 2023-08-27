name = input("")
cost = int(input(""))
mass = int(input(""))
money = int(input(""))
print(
    f"Чек\n{name} - {mass}кг - {cost}руб/кг\nИтого: {cost*mass}руб\nВнесено: {money}руб\nСдача: {money-(cost*mass)}руб"
)
