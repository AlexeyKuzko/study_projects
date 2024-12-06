n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

is_symmetric = all(matrix[i][j] == matrix[j][i] for i in range(n) for j in range(n))

print("YES" if is_symmetric else "NO")
