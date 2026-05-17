"""Solution for Stepik course solutions: Algorithms Data Structures / 3 Basic Data Structures / 3 Multidimensional Arrays And Matrices / Step 2."""

n = int(input())
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i + j == n - 1:
            matrix[i][j] = 1
        elif i + j > n - 1:
            matrix[i][j] = 2

for row in matrix:
    print(*row)
