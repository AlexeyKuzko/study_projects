n, m = map(int, input().split())

for i in range(1, n + 1):
    row = []
    for j in range(m):
        row.append(str(i + j * n).rjust(3))
    print(" ".join(row))
