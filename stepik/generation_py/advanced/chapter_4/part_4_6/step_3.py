"""Solution for Stepik course solutions: Generation Py / Advanced / Chapter 4 / Part 4 6 / Step 3."""

n, m = map(int, input().split())

counter = 1
for i in range(n):
    row = []
    for j in range(m):
        row.append(str(counter).rjust(3))
        counter += 1
    print(" ".join(row))
