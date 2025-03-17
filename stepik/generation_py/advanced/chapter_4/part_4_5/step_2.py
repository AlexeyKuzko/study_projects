n = int(input())
m = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

max_value = float("-inf")
max_row = None
max_col = None

for i in range(n):
    for j in range(m):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
            max_row = i
            max_col = j

print(max_row, max_col)
