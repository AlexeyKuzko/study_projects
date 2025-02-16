def generate_partitions(n, max_value, current_partition, result):
    if n == 0:
        result.append(current_partition[:])  # добавляем копию текущего разбиения
        return

    for i in range(min(n, max_value), 0, -1):
        current_partition.append(i)
        generate_partitions(n - i, i, current_partition, result)
        current_partition.pop()  # удаляем последний элемент для следующей итерации


def main():
    N = int(input().strip())
    result = []
    generate_partitions(N, N, [], result)

    # Выводим результаты в обратном порядке
    for partition in reversed(result):
        print(" ".join(map(str, partition)))


if __name__ == "__main__":
    main()
