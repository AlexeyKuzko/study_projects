n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

for row in matrix:
    avg = sum(row) / len(row)
    count = sum(1 for x in row if x > avg)
    print(count)
