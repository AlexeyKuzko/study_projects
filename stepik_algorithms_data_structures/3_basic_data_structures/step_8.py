def second_max():
    # Ввод количества чисел
    n = int(input())

    # Ввод массива чисел
    numbers = list(map(int, input().split()))

    # Инициализация max1 и max2
    max1 = max2 = float('-inf')

    # Обход массива чисел
    for num in numbers:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num != max1:
            max2 = num

    # Вывод второго по величине числа
    if max2 != float('-inf'):
        print(max2)
    else:
        print(None)

second_max()