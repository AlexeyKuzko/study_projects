def pascal(n, row):
    if row == 0:
        return [1]
    else:
        prev_row = pascal(n, row - 1)
        return [x + y for x, y in zip([0] + prev_row, prev_row + [0])]


n = int(input())
for i in range(n):
    print(*pascal(n, i), sep=" ")
