"""Solution for Stepik course solutions: Generation Py / Advanced / Chapter 5 / Step 3."""

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

for j in range(n):
    for i in range(n):
        print(matrix[i][j], end=" ")
    print()
