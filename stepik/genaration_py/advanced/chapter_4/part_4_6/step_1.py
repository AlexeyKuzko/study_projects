n, m = map(int, input().split())

for i in range(n):
    row = []
    for j in range(m):
        if (i + j) % 2 == 0:
            row.append('.')
        else:
            row.append('*')
    print(*row)