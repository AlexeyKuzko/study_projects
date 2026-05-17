"""Solution for Stepik course solutions: Algorithms Data Structures / 5 Search Algorithms / 1 Linear Search / Step 7."""

n = int(input())
a = list(map(int, input().split()))

count = 0
for i in range(1, n - 1):
    if a[i - 1] > a[i] < a[i + 1]:
        count += 1

print(count)
