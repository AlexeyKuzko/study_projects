import sys

input = sys.stdin.readline


def max_grass(n, terrain):
    # Массив для хранения максимального количества травы
    dp = [-float("inf")] * n
    dp[0] = 0  # Стартовая позиция

    for i in range(n):
        if dp[i] == -float("inf") or terrain[i] == "d":
            continue  # Пропускаем недостижимые или опасные клетки

        # Обновляем клетки, куда можно прыгнуть
        for jump in (1, 3, 5):
            if i + jump < n and terrain[i + jump] != "d":
                dp[i + jump] = max(
                    dp[i + jump], dp[i] + (1 if terrain[i + jump] == "g" else 0)
                )

    # Возвращаем результат для последней клетки
    return dp[n - 1] if dp[n - 1] != -float("inf") else -1


# Чтение входных данных
n = int(input().strip())
terrain = input().strip()

# Вывод результата
print(max_grass(n, terrain))
