"""Solution for Stepik course solutions: Generation Py / Advanced / Chapter 2 / Part 2 1 / 10 Step."""

n = int(input())
k = int(input())


def josephus(n, k):
    if n == 1:
        return 1
    else:
        return (josephus(n - 1, k) + k - 1) % n + 1


print(josephus(n, k))
