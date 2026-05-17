"""Solution for Stepik course solutions: Algorithms Data Structures / 3 Basic Data Structures / 3 Multidimensional Arrays And Matrices / Step 10."""

n, m = map(int, input().split())
a = [[0] * m for _ in range(n)]
num = 0
for i in range(n):
    if i % 2 == 0:
        for j in range(m):
            a[i][j] = num
            num += 1
    else:
        for j in range(m - 1, -1, -1):
            a[i][j] = num
            num += 1

for i in range(n):
    for j in range(m):
        print(f"{a[i][j]:3d}", end="")
    print()
