"""Solution for Stepik course solutions: Generation Py / Advanced / Chapter 4 / Part 4 6 / Step 1."""

n, m = map(int, input().split())

for i in range(n):
    row = []
    for j in range(m):
        if (i + j) % 2 == 0:
            row.append(".")
        else:
            row.append("*")
    print(*row)
