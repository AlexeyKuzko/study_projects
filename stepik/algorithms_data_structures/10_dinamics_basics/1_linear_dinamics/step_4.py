n = int(input())


def count_ways(n):
    dp = [0] * (n + 1)
    dp[0] = 1  # один способ остаться в нулевой ячейке

    for i in range(1, n + 1):
        dp[i] += dp[i - 1] if i - 1 >= 0 else 0
        dp[i] += dp[i - 3] if i - 3 >= 0 else 0
        dp[i] += dp[i - 4] if i - 4 >= 0 else 0

    return dp[n]


print(count_ways(n))
