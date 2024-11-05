import sys

input = sys.stdin.read

# Читаем данные
data = input().splitlines()
n = int(data[0])
a = list(map(int, data[1].split()))

# Массивы для хранения ответа
left_result = [0] * n
right_result = [0] * n

# Поиск ближайших меньших слева
left_stack = []
for i in range(n):
    while left_stack and left_stack[-1] >= a[i]:
        left_stack.pop()
    left_result[i] = left_stack[-1] if left_stack else 0
    left_stack.append(a[i])

# Поиск ближайших меньших справа
right_stack = []
for i in range(n - 1, -1, -1):
    while right_stack and right_stack[-1] >= a[i]:
        right_stack.pop()
    right_result[i] = right_stack[-1] if right_stack else 0
    right_stack.append(a[i])

# Вывод результатов
output = "\n".join(f"{left_result[i]} {right_result[i]}" for i in range(n))
print(output)
