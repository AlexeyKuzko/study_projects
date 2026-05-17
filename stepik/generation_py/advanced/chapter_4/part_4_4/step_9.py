"""Solution for Stepik course solutions: Generation Py / Advanced / Chapter 4 / Part 4 4 / Step 9."""

n = int(input())
m = int(input())

matrix = [input() for _ in range(n * m)]

for i in range(n):
    print(" ".join(matrix[i * m : (i + 1) * m]))

print()

for j in range(m):
    print(" ".join(matrix[k * m + j] for k in range(n)))
