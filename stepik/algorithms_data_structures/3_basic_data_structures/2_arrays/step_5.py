"""Solution for Stepik course solutions: Algorithms Data Structures / 3 Basic Data Structures / 2 Arrays / Step 5."""

n = int(input())  # Ввод количества чисел

# Ввод чисел в одну строку, разделенных пробелами, и преобразование их в список
numbers = list(map(int, input().split()))

# Вычисление суммы чисел
result = sum(numbers)

# Вывод результата
print(result)
