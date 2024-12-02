n = int(input())


def minimal_operations(n):
    dp = [0] * (n + 1)  # dp[i] — минимальное число операций для числа i
    prev = [0] * (n + 1)  # prev[i] — предыдущее число для восстановления пути

    for i in range(2, n + 1):
        # Обновляем dp[i] для каждой операции
        dp[i] = dp[i - 1] + 1
        prev[i] = i - 1

        if i % 2 == 0 and dp[i // 2] + 1 < dp[i]:
            dp[i] = dp[i // 2] + 1
            prev[i] = i // 2

        if i % 3 == 0 and dp[i // 3] + 1 < dp[i]:
            dp[i] = dp[i // 3] + 1
            prev[i] = i // 3

    # Восстанавливаем путь
    path = []
    current = n
    while current > 0:
        path.append(current)
        current = prev[current]

    path.reverse()  # Путь восстановлен в обратном порядке
    return dp[n], path


# Чтение входных данных

operations_count, sequence = minimal_operations(n)

# Вывод результата
print(operations_count)
print(*sequence)
