"""Solution for Stepik course solutions: Generation Py / Advanced / Chapter 4 / Part 4 5 / Step 4."""

n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

is_symmetric = all(matrix[i][j] == matrix[j][i] for i in range(n) for j in range(n))

print("YES" if is_symmetric else "NO")
