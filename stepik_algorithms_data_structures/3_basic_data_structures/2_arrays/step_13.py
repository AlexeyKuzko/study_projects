def count_elements():
    # Ввод количества элементов и массива чисел
    n = int(input())
    numbers = list(map(int, input().split()))

    # Инициализировать переменную count
    count = 0

    # Перебрать элементы массива
    for i in range(1, n - 1):
        # Проверить, является ли элемент больше обоих своих соседей
        if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
            # Инкрементировать переменную count
            count += 1

    # Вывести значение переменной count
    print(count)

count_elements()