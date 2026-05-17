"""Solution for Stepik course solutions: Generation Py / Advanced / Chapter 4 / Part 4 5 / Step 7."""

n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

rotated_matrix = [list(reversed(i)) for i in zip(*matrix)]

for row in rotated_matrix:
    print(*row)
