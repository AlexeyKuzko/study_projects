"""Solution for Stepik course solutions: Algorithms Data Structures / 2 Algorithms Computing Models / 4 Recursion / Step 12."""


def countZeros(n):
    if n < 10:
        if n == 0:
            return 1
        else:
            return 0
    else:
        return (n % 10 == 0) + countZeros(n // 10)


n = int(input())
print(countZeros(n))
