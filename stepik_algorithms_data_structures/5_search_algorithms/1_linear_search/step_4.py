def find_min_max(arr):
    """
    Функция находит минимальное и максимальное значения в списке arr.
    """
    if not arr:
        return None, None  # Обработка пустого списка

    min_value = arr[0]
    max_value = arr[0]

    for num in arr:
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num

    return min_value, max_value


# Считываем входные данные
n = int(input())
arr = list(map(int, input().split()))

# Вызываем функцию find_min_max и выводим результат
min_value, max_value = find_min_max(arr)
print(min_value)
print(max_value)
