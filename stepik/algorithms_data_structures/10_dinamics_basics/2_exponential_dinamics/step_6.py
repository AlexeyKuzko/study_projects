def longest_common_subsequence(a, b, c):
    n, m, k = len(a), len(b), len(c)
    dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for p in range(1, k + 1):
                if a[i - 1] == b[j - 1] == c[p - 1]:
                    dp[i][j][p] = dp[i - 1][j - 1][p - 1] + 1
                else:
                    dp[i][j][p] = max(dp[i - 1][j][p], dp[i][j - 1][p], dp[i][j][p - 1])

    return dp[n][m][k]


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    k = int(input())
    c = list(map(int, input().split()))
    print(longest_common_subsequence(a, b, c))
