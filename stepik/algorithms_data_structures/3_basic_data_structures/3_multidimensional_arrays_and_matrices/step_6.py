def solve():
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    rotated_matrix = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            rotated_matrix[j][n - 1 - i] = matrix[i][j]

    print(m, n)
    for row in rotated_matrix:
        print(*row)


solve()
