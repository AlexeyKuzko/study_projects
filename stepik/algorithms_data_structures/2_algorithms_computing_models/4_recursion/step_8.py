"""Solution for Stepik course solutions: Algorithms Data Structures / 2 Algorithms Computing Models / 4 Recursion / Step 8."""


def countDigits(n):
    n = abs(n)
    if n < 10:
        return 1
    else:
        return 1 + countDigits(n // 10)


n = int(input())
print(countDigits(n))
