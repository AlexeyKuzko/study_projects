"""Solution for Stepik course solutions: Algorithms Data Structures / 2 Algorithms Computing Models / 4 Recursion / Step 10."""


def hanoi(n, source, auxiliary, target):
    if n > 0:
        hanoi(n - 1, source, target, auxiliary)
        print(f"Переместите диск с {source} на {target}")
        hanoi(n - 1, auxiliary, source, target)


N = int(input())

hanoi(N, 1, 2, 3)
