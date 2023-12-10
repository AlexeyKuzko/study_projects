# Problem A
def problem_a():
    print("Привет, Яндекс!")


problem_a()


# Problem B
def problem_b():
    username = input("Как Вас зовут?")
    print(f"""Привет, {username}""")


problem_b()


# Problem C
def problem_c():
    information = input("")
    print(f"{information}\n{information}\n{information}\n")


problem_c()


# Problem D
def problem_d():
    income = int(input(""))
    print(f"{int(income - (38 * 2.5))}")


problem_d()

# Problem E
price = int(input(""))
weight = int(input(""))
money = int(input(""))
print(f"{money - (price * weight)}")

# Problem F
name = input("")
cost = int(input(""))
mass = int(input(""))
money = int(input(""))
print(
    f"Чек\n{name} - {mass}кг - {cost}руб/кг\nИтого: {cost * mass}руб\nВнесено: {money}руб\nСдача: {money - (cost * mass)}руб"
)

# Problem G
repeat = int(input(""))
print("Купи слона!\n" * repeat)

# Problem H
repeat = int(input(""))
punishment = input("")
print(f'Я больше никогда не буду писать "{punishment}"!\n' * repeat)

# Problem I
M = int(input(""))
N = int(input(""))

calc = (2 / 2) / 2
total = int(M * calc * N)

print(total)

# Problem J
name = input("")
number = input("")
group = number[0]
child_number = number[2]
bed = number[1]

print(
    f"""Группа №{group}.
{child_number}. {name}.  
Шкафчик: {number}.  
Кроватка: {bed}."""
)

# Problem K
number = input("")

print(f"""{int(number[1])}{int(number[0])}{int(number[3])}{int(number[2])}""")


# Problem L
def sum_without_carry(num1, num2):
    results = 0
    scale = 1
    while num1 > 0 or num2 > 0:
        digit1 = num1 % 10
        digit2 = num2 % 10

        sum_digits = (digit1 + digit2) % 10
        results += sum_digits * scale

        num1 //= 10
        num2 //= 10
        scale *= 10
    return results


input1 = int(input(""))
input2 = int(input(""))
result = sum_without_carry(input1, input2)
print(result)

# Problem M
children = int(input(""))
chocolates = int(input(""))
print(f"{chocolates // children}\n{chocolates % children}")

# Problem N
red = int(input(""))
green = int(input(""))
blue = int(input(""))
print(red + blue + 1)

# Problem O
start_hours = int(input(""))
start_minutes = int(input(""))
wait_minutes = int(input(""))

total_minutes = start_minutes + wait_minutes
total_hours = total_minutes // 60
total_minutes = total_minutes % 60

if total_hours == 0:
    print("{:02d}:{:02d}".format(total_hours, total_minutes))
else:
    total_hours += start_hours
    while total_hours >= 24:
        total_hours -= 24
    print("{:02d}:{:02d}".format(total_hours, total_minutes))

# Problem P
a_km = int(input(""))
b_km = int(input(""))
c_kmh = int(input(""))
print(f"{(b_km - a_km) / c_kmh:.2f}")

# Problem Q
decimal = int(input(""))
binary = input("")
binary_decimal = int(binary, 2)
result = decimal + binary_decimal

print(result)

# Problem R
binary = input("")
decimal = int(input(""))
binary_decimal = int(binary, 2)
result = binary_decimal - decimal

print(result * (-1))

# Problem S
name = input("")
cost = int(input(""))
mass = int(input(""))
money = int(input(""))
price_output = str(str(mass) + "кг * " + str(cost) + "руб/кг")
print(f"{'=' * 16}Чек{'=' * 16}")
print(f"Товар:{name: >29}")
print(f"Цена:{price_output:>30}")
print(f"Итого:{cost * mass: >26}руб")
print(f"Внесено:{money: >24}руб")
print(f"Сдача:{money - cost * mass: >26}руб")
print(f"{'=' * 35}")

# Problem T
N = int(input(""))
M = int(input(""))
K1 = int(input(""))
K2 = int(input(""))
m1 = N * (K2 - M) / (K2 - K1)
m2 = N - m1
print(int(m1), int(m2))
