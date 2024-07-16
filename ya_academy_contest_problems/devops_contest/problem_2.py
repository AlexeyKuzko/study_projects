# Чтение входных данных
n = int(input().strip())
a = list(map(int, input().strip().split()))

# Вычисление количества сравнений
def count_insertion_sort_comparisons(n, a):
    comparisons = 0
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            comparisons += 1
            a[j + 1] = a[j]
            j -= 1
        comparisons += (j >= 0)  # для последнего сравнения когда a[j] <= key или j < 0
        a[j + 1] = key
    return comparisons
result = count_insertion_sort_comparisons(n, a)

# Вывод результата
print(result)