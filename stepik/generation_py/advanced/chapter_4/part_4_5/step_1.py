"""Solution for Stepik course solutions: Generation Py / Advanced / Chapter 4 / Part 4 5 / Step 1."""

n = int(input())
m = int(input())

mult = [[i * j for j in range(m)] for i in range(n)]

for row in mult:
    print(" ".join(str(x).ljust(3) for x in row))
