"""Solution for Stepik course solutions: Algorithms Data Structures / 12 Graphs / Step 7."""

n = int(input())
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    k, *edges = map(int, input().split())
    for edge in edges:
        matrix[i][edge - 1] = 1

for row in matrix:
    print(*row)
