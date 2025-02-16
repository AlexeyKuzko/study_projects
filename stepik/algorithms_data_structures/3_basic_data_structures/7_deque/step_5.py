from collections import deque
import sys

input = sys.stdin.read
data = input().strip().splitlines()

# Инициализация
n = int(data[0])
commands = data[1:]
shelf = deque()
results = []

# Обработка команд
for command in commands:
    parts = command.split()
    op_type = int(parts[0])

    if op_type == 1:  # Поставить слева
        book_id = int(parts[1])
        shelf.appendleft(book_id)
    elif op_type == 2:  # Поставить справа
        book_id = int(parts[1])
        shelf.append(book_id)
    elif op_type == 3:  # Убрать слева
        results.append(shelf.popleft())
    elif op_type == 4:  # Убрать справа
        results.append(shelf.pop())

# Вывод всех результатов команд 3 и 4
print("\n".join(map(str, results)))
