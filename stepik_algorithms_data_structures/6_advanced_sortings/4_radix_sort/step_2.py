def sort_pairs(pairs):
    # Сортируем пары по первому элементу
    sorted_pairs = sorted(pairs, key=lambda x: x[0])
    return sorted_pairs


if __name__ == "__main__":
    import sys

    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    pairs = [(int(data[2 * i + 1]), int(data[2 * i + 2])) for i in range(n)]

    sorted_pairs = sort_pairs(pairs)

    for pair in sorted_pairs:
        print(pair[0], pair[1])
