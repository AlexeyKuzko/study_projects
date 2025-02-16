import sys

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))


def merge_sort(a):
    if len(a) <= 1:
        return a, 0
    mid = len(a) // 2
    left, inv_left = merge_sort(a[:mid])
    right, inv_right = merge_sort(a[mid:])
    merged, inv_merge = merge(left, right)
    return merged, inv_left + inv_right + inv_merge


def merge(left, right):
    result = []
    inv_count = 0
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            inv_count += len(left) - i
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result, inv_count


sorted_a, inversions = merge_sort(a)
print(inversions)
