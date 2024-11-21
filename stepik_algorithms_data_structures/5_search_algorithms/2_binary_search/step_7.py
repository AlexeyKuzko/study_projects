def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False


def solve():
    m = int(input())
    arr = list(map(int, input().split()))
    n = int(input())

    if binary_search(arr, n):
        print("YES")
    else:
        print("NO")


solve()
