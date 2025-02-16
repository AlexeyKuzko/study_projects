def max_worm_length(n, k, lengths):
    def can_divide(length):
        count = sum(l // length for l in lengths)
        return count >= k

    low, high = 1, max(lengths)  # Изменили low на 1
    best_length = 0

    while low <= high:
        mid = (low + high) // 2
        if can_divide(mid):
            best_length = mid
            low = mid + 1
        else:
            high = mid - 1

    return best_length


import sys

input = sys.stdin.read
data = input().split()
n = int(data[0])
k = int(data[1])
lengths = list(map(int, data[2:]))
print(max_worm_length(n, k, lengths))
