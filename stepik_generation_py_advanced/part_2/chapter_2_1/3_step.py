mass = float(input())
height = float(input())
bmi = mass / height**2

if bmi < 18.5:
    print("Недостаточная масса")
elif 18.5 <= bmi <= 25:
    print("Оптимальная масса")
elif 25 < bmi:
    print("Избыточная масса")
