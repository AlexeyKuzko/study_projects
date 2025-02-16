def linear_search(arr, target):
    """
    Функция выполняет линейный поиск в списке arr и возвращает индекс первого
    вхождения целевого значения target. Если значение не найдено, возвращает -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Считываем входные данные
n = int(input())
arr = list(map(int, input().split()))
target = int(input())

# Вызываем функцию linear_search и выводим результат
result = linear_search(arr, target)
print(result)
