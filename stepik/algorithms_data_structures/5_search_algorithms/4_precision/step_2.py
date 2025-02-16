from decimal import Decimal, getcontext

# Устанавливаем точность вычислений
getcontext().prec = 40


def calculate_sum(n, a):
    total_sum = Decimal(0)

    for num in a:
        ai = Decimal(num)
        total_sum += ai + (1 / ai)

    return total_sum


# Чтение входных данных
import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
a = list(map(int, data[1:]))

# Вычисление и вывод результата
result = calculate_sum(n, a)
print(f"{result:.20f}")
