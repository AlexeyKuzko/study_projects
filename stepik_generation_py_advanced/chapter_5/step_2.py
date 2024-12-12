n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

max_element = float("-inf")
for i in range(n):
    for j in range(n):
        if i + j >= n - 1:
            max_element = max(max_element, matrix[i][j])

print(max_element)
