n = int(input())

matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

m = int(input())


def multiply(matrix1, matrix2):
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for t in range(n):
                result[i][j] += matrix1[i][t] * matrix2[t][j]
    return result


def power(matrix, m):
    if m == 1:
        return matrix
    if m % 2 == 0:
        half_pow = power(matrix, m // 2)
        return multiply(half_pow, half_pow)
    else:
        half_pow = power(matrix, m // 2)
        return multiply(multiply(half_pow, half_pow), matrix)


result = power(matrix, m)

for row in result:
    print(" ".join(map(str, row)))
