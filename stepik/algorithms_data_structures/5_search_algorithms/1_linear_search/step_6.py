def find_smallest_duplicate(arr):
    """
    Функция находит наименьший элемент, который повторяется в списке arr.
    """
    counts = {}  # Словарь для хранения частот элементов
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    duplicates = []
    for num, count in counts.items():
        if count >= 2:
            duplicates.append(num)

    if not duplicates:
        return "NO"
    else:
        return min(duplicates)


# Считываем входные данные
n = int(input())
arr = list(map(int, input().split()))

# Вызываем функцию find_smallest_duplicate и выводим результат
result = find_smallest_duplicate(arr)
print(result)
