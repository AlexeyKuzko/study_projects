def calculate(n, memo={}):
    if n <= 1:
        return 1
    if n in memo:
        return memo[n]

    initial_value = (n * n) // 3 + calculate(n - 2, memo)
    while initial_value % 2 == 0:
        initial_value //= 2

    initial_value += calculate(2 * n // 3, memo)
    value = calculate(initial_value % n, memo)

    result = value + calculate(n // 2, memo) + n
    memo[n] = result
    return result


n = int(input())
print(calculate(n))
