import sys

input = sys.stdin.read


def solve_cube_sum():
    data = input().split()
    t = int(data[0])  # Количество тестов
    tests = list(map(int, data[1:]))

    max_n = max(tests)  # Максимальное значение среди всех тестов

    # Предварительный расчет dp для всех чисел от 1 до max_n
    dp = [float("inf")] * (max_n + 1)
    dp[0] = 0

    # Список кубов, которые меньше max_n
    cubes = []
    k = 1
    while k**3 <= max_n:
        cubes.append(k**3)
        k += 1

    # Заполняем массив dp
    for x in range(1, max_n + 1):
        for cube in cubes:
            if cube > x:
                break
            dp[x] = min(dp[x], dp[x - cube] + 1)

    # Выводим результаты для всех тестов
    results = [str(dp[n]) for n in tests]
    sys.stdout.write("\n".join(results) + "\n")


solve_cube_sum()
