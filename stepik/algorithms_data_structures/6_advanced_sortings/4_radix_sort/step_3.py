import sys

def sort_strings(n, strings):
    # Сортировка по последнему символу
    strings.sort(key=lambda x: x[2])
    print(' '.join(strings))

    # Сортировка по второму символу
    strings.sort(key=lambda x: x[1])
    print(' '.join(strings))

    # Сортировка по первому символу
    strings.sort(key=lambda x: x[0])
    print(' '.join(strings))

if __name__ == "__main__":
    n = int(input())
    strings = input().split()
    sort_strings(n, strings)