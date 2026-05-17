"""Solution for Stepik course solutions: Generation Py / Advanced / Chapter 4 / Part 4 6 / Step 5."""

n = int(input())

for i in range(n):
    row = []
    for j in range(n):
        if i == j or i + j == n - 1:
            row.append("1")
        else:
            row.append("0")
    print(" ".join(map(str.ljust, row, [3] * n)))
