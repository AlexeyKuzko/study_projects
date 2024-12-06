n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

matrix = matrix[::-1]

for row in matrix:
    print(*row)
