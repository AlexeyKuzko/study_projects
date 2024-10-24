def reverse_permutation():
    # Ввод количества элементов и массива чисел
    n = int(input())
    numbers = list(map(int, input().split()))

    # Создать новый массив reverse_permutation
    reverse_permutation = [0] * n

    # Перебрать элементы массива numbers
    for i, num in enumerate(numbers):
        # Поставить в соответствующую позицию в массиве reverse_permutation значение i + 1
        reverse_permutation[num - 1] = i + 1

    # Вывести массив reverse_permutation
    print(' '.join(map(str, reverse_permutation)))

reverse_permutation()