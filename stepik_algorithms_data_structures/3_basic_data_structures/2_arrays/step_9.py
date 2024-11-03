def transform_array():
    # Ввод массива чисел
    numbers = list(map(int, input().split()))

    # Найти минимальное значение
    min_val = min(numbers)

    # Найти индекс минимального значения
    min_index = numbers.index(min_val)

    # Найти максимальное значение
    max_val = max(numbers)

    # Обойти массив чисел и вычесть max_val из элементов, идущих после min_val
    for i in range(min_index + 1, len(numbers)):
        numbers[i] -= max_val

    # Вывести преобразованный массив
    print(' '.join(map(str, numbers)))

transform_array()