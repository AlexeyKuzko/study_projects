"""Solution for Stepik course solutions: Algorithms Data Structures / 3 Basic Data Structures / 2 Arrays / Step 12."""


def shift_array():
    # Ввод количества элементов и массива чисел
    n = int(input())
    numbers = list(map(int, input().split()))

    # Ввод количества шагов для сдвига массива вправо
    k = int(input())

    # Сдвинуть массив вправо на k шагов, используя срезы
    k = k % n  # Обработка случая, когда k больше n
    shifted_numbers = numbers[-k:] + numbers[:-k]

    # Вывести преобразованный массив
    print(" ".join(map(str, shifted_numbers)))


shift_array()
