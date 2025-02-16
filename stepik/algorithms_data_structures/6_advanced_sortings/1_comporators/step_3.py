def optimal_point(n, a):
    a.sort()
    median_index = n // 2
    return a[median_index]


if __name__ == "__main__":
    import sys

    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    a = list(map(int, data[1:]))
    print(optimal_point(n, a))
