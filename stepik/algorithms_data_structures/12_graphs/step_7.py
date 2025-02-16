n = int(input())
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    k, *edges = map(int, input().split())
    for edge in edges:
        matrix[i][edge - 1] = 1

for row in matrix:
    print(*row)