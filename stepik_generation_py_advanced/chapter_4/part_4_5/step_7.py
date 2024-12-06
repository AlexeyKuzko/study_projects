n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

rotated_matrix = [list(reversed(i)) for i in zip(*matrix)]

for row in rotated_matrix:
    print(*row)
