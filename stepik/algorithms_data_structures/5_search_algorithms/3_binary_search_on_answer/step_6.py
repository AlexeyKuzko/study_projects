def can_place_points(a, n, k, min_dist):
    count = 1  # первый элемент всегда выбирается
    last_position = a[0]

    for i in range(1, n):
        if a[i] - last_position >= min_dist:
            count += 1
            last_position = a[i]
            if count == k:
                return True
    return False


def find_max_min_distance(n, k, a):
    a.sort()

    left = 0
    right = a[-1] - a[0]
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if can_place_points(a, n, k, mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result


# Чтение входных данных
import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
k = int(data[1])
a = list(map(int, data[2:]))

# Поиск оптимального решения
answer = find_max_min_distance(n, k, a)
print(answer)
