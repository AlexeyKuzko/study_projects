def quickselect(arr, L, R, k, depth, r):
    if L == R:
        return arr[L]

    pivot_index = L + r[depth] % (R - L + 1)
    pivot = arr[pivot_index]

    # Partition step
    less = []
    equal = []
    greater = []

    for i in range(L, R + 1):
        if arr[i] < pivot:
            less.append(arr[i])
        elif arr[i] == pivot:
            equal.append(arr[i])
        else:
            greater.append(arr[i])

    # Reconstruct array based on partition
    arr[L : R + 1] = less + equal + greater

    # Determine the range of indices for less, equal, and greater
    less_len = len(less)
    equal_len = len(equal)

    if k < L + less_len:
        # k-th statistic is in the "less" part
        return quickselect(arr, L, L + less_len - 1, k, depth + 1, r)
    elif k < L + less_len + equal_len:
        # k-th statistic is in the "equal" part
        return arr[L + less_len]
    else:
        # k-th statistic is in the "greater" part
        return quickselect(arr, L + less_len + equal_len, R, k, depth + 1, r)


if __name__ == "__main__":
    import sys

    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    k = int(data[1])
    arr = list(map(int, data[2 : n + 2]))
    r = list(map(int, data[n + 2 :]))

    # Note that k is 1-based, so we convert it to 0-based for our implementation
    k_stat = quickselect(arr, 0, n - 1, k - 1, 0, r)

    print(k_stat)
    print(" ".join(map(str, arr)))
