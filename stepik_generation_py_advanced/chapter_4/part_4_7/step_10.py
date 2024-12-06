n, m = map(int, input().split())

matrix1 = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix1.append(row)

input()  # пустая строка

m, k = map(int, input().split())

matrix2 = []
for _ in range(m):
    row = list(map(int, input().split()))
    matrix2.append(row)

result = [[0 for _ in range(k)] for _ in range(n)]

for i in range(n):
    for j in range(k):
        for t in range(m):
            result[i][j] += matrix1[i][t] * matrix2[t][j]

for row in result:
    print(' '.join(map(str, row)))