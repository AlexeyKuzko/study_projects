n, m = map(int, input().split())
a = [[0] * m for _ in range(n)]
num = 0
for k in range(n + m - 1):
    for i in range(n):
        for j in range(m):
            if i + j == k:
                a[i][j] = num
                num += 1

for i in range(n):
    for j in range(m):
        print(f'{a[i][j]:3d}', end='')
    print()