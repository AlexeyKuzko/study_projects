def count_number():
    # Ввод количества чисел
    n = int(input())

    # Ввод списка чисел
    numbers = list(map(int, input().split()))

    # Ввод числа, которое нужно посчитать
    number = int(input())

    # Создание словаря для хранения количества вхождений каждого числа
    count_dict = {}

    # Обход списка чисел и обновление словаря
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # Вывод количества вхождений искомого числа
    print(count_dict.get(number, 0))

count_number()