def sort_pairs(n, pairs):
    # Добавляем к каждой паре ее номер
    pairs_with_index = [(pair[0], pair[1], i + 1) for i, pair in enumerate(pairs)]
    # Сортируем пары по правилам из условия
    sorted_pairs = sorted(pairs_with_index, key=lambda x: (x[0], x[1], x[2]))
    # Возвращаем номера пар в отсортированном порядке
    return [pair[2] for pair in sorted_pairs]


n = int(input())
pairs = [list(map(int, input().split())) for _ in range(n)]

result = sort_pairs(n, pairs)
print(*result)
