def find_most_frequent_element(arr):
    """
    Функция находит элемент с наибольшей частотой в списке arr.
    """
    counts = {}  # Словарь для хранения частот элементов
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    most_frequent_element = None
    max_count = 0
    for num, count in counts.items():
        if count > max_count:
            max_count = count
            most_frequent_element = num

    return most_frequent_element


# Считываем входные данные
n = int(input())
arr = list(map(int, input().split()))

# Вызываем функцию find_most_frequent_element и выводим результат
most_frequent_element = find_most_frequent_element(arr)
print(most_frequent_element)
