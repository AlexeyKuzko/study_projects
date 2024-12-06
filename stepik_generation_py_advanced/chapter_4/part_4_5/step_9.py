n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

expected_sum = sum(matrix[0])

# Проверяем строки
for row in matrix:
    if sum(row) != expected_sum:
        print("NO")
        exit()

# Проверяем столбцы
for col in range(n):
    if sum(matrix[row][col] for row in range(n)) != expected_sum:
        print("NO")
        exit()

# Проверяем главную диагональ
if sum(matrix[i][i] for i in range(n)) != expected_sum:
    print("NO")
    exit()

# Проверяем побочную диагональ
if sum(matrix[i][n - i - 1] for i in range(n)) != expected_sum:
    print("NO")
    exit()

# Проверяем, что все числа от 1 до n^2 присутствуют ровно один раз
if sorted([matrix[i][j] for i in range(n) for j in range(n)]) != list(
    range(1, n * n + 1)
):
    print("NO")
    exit()

print("YES")
