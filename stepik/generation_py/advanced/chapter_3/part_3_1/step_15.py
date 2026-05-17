"""Solution for Stepik course solutions: Generation Py / Advanced / Chapter 3 / Part 3 1 / Step 15."""


def func(num1, num2):
    return num1 % num2 == 0


# Считывание входных данных
num1 = int(input())
num2 = int(input())

# Проверка и вывод результата
if func(num1, num2):
    print("делится")
else:
    print("не делится")
