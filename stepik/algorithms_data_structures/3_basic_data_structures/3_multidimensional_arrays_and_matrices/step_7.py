def solve():
    n, m = map(int, input().split())

    if n == 1 and m == 1:
        print(1)
    elif n == 1:
        print(1)
    elif m == 1:
        print(1)
    else:
        print(factorial(n + m - 2) // (factorial(n - 1) * factorial(m - 1)))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


solve()
