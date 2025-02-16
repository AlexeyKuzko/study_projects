import functools


def compare(x, y):
    # Компаратор для сортировки строк
    if x + y < y + x:
        return -1
    elif x + y > y + x:
        return 1
    else:
        return 0


def lexicographically_minimal_string(n, strings):
    # Сортируем строки с использованием компаратора
    sorted_strings = sorted(strings, key=functools.cmp_to_key(compare))
    # Склеиваем отсортированные строки
    return "".join(sorted_strings)


def main():
    import sys

    input = sys.stdin.read
    data = input().split()

    index = 0
    num_tests = int(data[index])
    index += 1
    results = []

    for _ in range(num_tests):
        n = int(data[index])
        index += 1
        strings = data[index : index + n]
        index += n
        results.append(lexicographically_minimal_string(n, strings))

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
