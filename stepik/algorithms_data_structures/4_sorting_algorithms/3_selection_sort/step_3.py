"""Solution for Stepik course solutions: Algorithms Data Structures / 4 Sorting Algorithms / 3 Selection Sort / Step 3."""

n = int(input())
a = list(map(int, input().split()))


def selection_sort(a):
    for i in range(len(a)):
        min_idx = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


print(*selection_sort(a))
