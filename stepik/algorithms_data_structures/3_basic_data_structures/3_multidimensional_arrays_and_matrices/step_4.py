"""Solution for Stepik course solutions: Algorithms Data Structures / 3 Basic Data Structures / 3 Multidimensional Arrays And Matrices / Step 4."""

n = int(input())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

is_symmetric = True
for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            is_symmetric = False
            break
    if not is_symmetric:
        break

if is_symmetric:
    print("yes")
else:
    print("no")
