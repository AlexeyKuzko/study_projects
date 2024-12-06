n, m = map(int, input().split())

matrix1 = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix1.append(row)

input()  # пустая строка

matrix2 = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix2.append(row)

result = [[matrix1[i][j] + matrix2[i][j] for j in range(m)] for i in range(n)]

for row in result:
    print(' '.join(map(str, row)))