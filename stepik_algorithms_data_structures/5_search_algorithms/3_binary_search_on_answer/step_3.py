N = float(input())


def sqrt_binary_search(N):
    if N == 0:
        return 0.0

    low = 0.0
    high = max(1.0, N)
    epsilon = 0.0000001

    while high - low > epsilon:
        mid = (low + high) / 2.0
        if mid * mid < N:
            low = mid
        else:
            high = mid

    result = round(mid, 3)
    return "{:.3f}".format(result)


print(sqrt_binary_search(N))
