"""Solution for Stepik course solutions: Generation Py / Advanced / Chapter 4 / Part 4 5 / Step 6."""

n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

matrix = matrix[::-1]

for row in matrix:
    print(*row)
