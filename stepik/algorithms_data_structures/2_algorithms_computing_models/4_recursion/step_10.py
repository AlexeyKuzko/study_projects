def hanoi(n, source, auxiliary, target):
    if n > 0:
        hanoi(n - 1, source, target, auxiliary)
        print(f"Переместите диск с {source} на {target}")
        hanoi(n - 1, auxiliary, source, target)

N = int(input())

hanoi(N, 1, 2, 3)