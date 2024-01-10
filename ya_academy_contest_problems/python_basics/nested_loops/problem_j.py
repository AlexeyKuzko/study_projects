def divide_orange(n):
    for a in range(1, n):
        for b in range(1, n - a):
            c = n - a - b
            if c >= 1:
                print(f"{a} {b} {c}")

segments = int(input())
print(f"А Б В")
divide_orange(segments)