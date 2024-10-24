n = int(input()) # Ввод количества чисел

# Ввод чисел в одну строку, разделенных пробелами, и преобразование их в список
numbers = list(map(int, input().split()))

# Вычисление суммы чисел
result = sum(numbers)

# Вывод результата
print(result)
