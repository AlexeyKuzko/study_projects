n = int(input())

for i in range(n):
    row = []
    for j in range(n):
        if i == j or i + j == n - 1:
            row.append("1")
        else:
            row.append("0")
    print(" ".join(map(str.ljust, row, [3] * n)))
