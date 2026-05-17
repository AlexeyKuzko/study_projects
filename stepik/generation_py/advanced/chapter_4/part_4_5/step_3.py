"""Solution for Stepik course solutions: Generation Py / Advanced / Chapter 4 / Part 4 5 / Step 3."""

n = int(input())
m = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

i, j = map(int, input().split())

for row in matrix:
    row[i], row[j] = row[j], row[i]

for row in matrix:
    print(*row)
