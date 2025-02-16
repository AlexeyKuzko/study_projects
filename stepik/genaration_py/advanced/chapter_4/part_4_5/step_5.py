n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    matrix[i][i], matrix[i][n - i - 1] = matrix[i][n - i - 1], matrix[i][i]

for row in matrix:
    print(*row)
