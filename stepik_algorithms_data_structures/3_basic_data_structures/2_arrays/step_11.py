def transform_array():
    # Ввод массива чисел
    numbers = list(map(int, input().split()))

    # Найти индексы минимального и максимального значений
    min_index = numbers.index(min(numbers))
    max_index = numbers.index(max(numbers))

    # Переставить элементы между минимальным и максимальным значениями в обратном порядке
    if min_index < max_index:
        numbers[min_index:max_index+1] = numbers[min_index:max_index+1][::-1]
    else:
        numbers[max_index:min_index+1] = numbers[max_index:min_index+1][::-1]

    # Вывести преобразованный массив
    print(' '.join(map(str, numbers)))

transform_array()