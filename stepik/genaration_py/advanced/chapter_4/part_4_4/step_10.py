n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

trace = sum(matrix[i][i] for i in range(n))

print(trace)
