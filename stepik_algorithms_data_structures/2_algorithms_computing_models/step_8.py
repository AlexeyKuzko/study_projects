def countDigits(n):
    n = abs(n)
    if n < 10:
        return 1
    else:
        return 1 + countDigits(n // 10)

n = int(input())
print(countDigits(n))