import sys
from sortedcontainers import SortedList

input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

# Инициализируем два указателя и список для хранения элементов
left = 0
min_length = float('inf')
current_window = SortedList()

for right in range(n):
    current_window.add(a[right])
    
    while current_window[-1] - current_window[0] >= k:
        min_length = min(min_length, right - left + 1)
        current_window.remove(a[left])
        left += 1

# Если min_length не обновился, значит подходящего отрезка не существует
print(min_length if min_length != float('inf') else 0)
