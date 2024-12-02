def knapsack(n, S, weights):
    dp = [0] * (S + 1)
    for weight in weights:
        for i in range(S, weight - 1, -1):
            dp[i] = max(dp[i], dp[i - weight] + weight)
    return dp[S]


t = int(input())
for _ in range(t):
    n, S = map(int, input().split())
    weights = list(map(int, input().split()))
    print(knapsack(n, S, weights))
