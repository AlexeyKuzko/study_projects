def transform_array():
    # Ввод массива чисел
    numbers = list(map(int, input().split()))

    # Считать количество отрицательных и положительных чисел
    neg_count = sum(1 for num in numbers if num < 0)
    pos_count = sum(1 for num in numbers if num >= 0)

    # Обойти массив чисел и вычесть количество отрицательных чисел из количества положительных чисел и наоборот
    for i, num in enumerate(numbers):
        if num < 0:
            numbers[i] -= pos_count
        else:
            numbers[i] -= neg_count

    # Вывести преобразованный массив
    print(' '.join(map(str, numbers)))

transform_array()