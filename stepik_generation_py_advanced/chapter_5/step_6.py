def is_latin_square(matrix, n):
    # Проверяем строки
    for row in matrix:
        if len(set(row)) != n or any(x < 1 or x > n for x in row):
            return False

    # Проверяем столбцы
    for col in range(n):
        column_values = {matrix[row][col] for row in range(n)}
        if len(column_values) != n:
            return False

    return True


# Чтение входных данных
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Проверка на латинский квадрат
if is_latin_square(matrix, n):
    print("YES")
else:
    print("NO")
