import sys

# Читаем n, q, a       
input = sys.stdin.readline
n, q = map(int, input().split())
a = list(map(int, input().split()))

# Предподсчёт префиксных сумм
prefix_sums = [0] * (n + 1)
for i in range(1, n + 1):
  prefix_sums[i] = prefix_sums[i - 1] + a[i - 1]

#print(f"n={n}, q={q}, a={a}") # Дебаг-вывод, закомментируйте перед отправкой решения

total_sum = 0
# Читаем все запросы
for _ in range(q):
  l, r = map(int, input().split())
  
  # Обработка запроса [l,r]
  segment_sum = prefix_sums[r] - prefix_sums[l - 1]
  total_sum += segment_sum

  #print(f"query l={l} r={r}") # Дебаг-вывод, закомментируйте перед отправкой решения

print(total_sum) 