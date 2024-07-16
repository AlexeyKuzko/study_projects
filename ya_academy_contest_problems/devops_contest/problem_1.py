# Прочитать количество пар
n = int(input().strip())
# Формирование списка пар
pairs = []
for _ in range(n):
    a, b = map(int, input().strip().split())
    pairs.append((a, b))

# Получение отсортированных индексов
def sort_and_get_indices(n, pairs):
    # Добавляем индексы к парам для сохранения оригинального порядка
    indexed_pairs = [(pair[0], pair[1], index + 1) for index, pair in enumerate(pairs)]
    # Выполним сортировку по первым элементам, затем по вторым, затем по оригинальным индексам
    sorted_pairs = sorted(indexed_pairs, key=lambda x: (x[0], x[1], x[2]))
    # Извлечем индексы после сортировки
    sorted_indices = [pair[2] for pair in sorted_pairs]
    return sorted_indices
sorted_indices = sort_and_get_indices(n, pairs)

# Вывод результата
print(" ".join(map(str, sorted_indices)))