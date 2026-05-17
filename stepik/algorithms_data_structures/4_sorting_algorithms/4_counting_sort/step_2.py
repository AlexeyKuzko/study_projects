"""Solution for Stepik course solutions: Algorithms Data Structures / 4 Sorting Algorithms / 4 Counting Sort / Step 2."""

n = int(input())
a = list(map(int, input().split()))

count = [0] * 15001
for mark in a:
    count[mark] += 1


missing = sum(1 for x in count[1:] if x == 0)
print(missing)
