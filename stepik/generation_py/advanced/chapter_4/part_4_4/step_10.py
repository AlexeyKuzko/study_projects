"""Solution for Stepik course solutions: Generation Py / Advanced / Chapter 4 / Part 4 4 / Step 10."""

n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

trace = sum(matrix[i][i] for i in range(n))

print(trace)
