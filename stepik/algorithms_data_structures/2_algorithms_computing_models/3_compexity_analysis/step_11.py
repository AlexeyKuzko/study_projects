"""Solution for Stepik course solutions: Algorithms Data Structures / 2 Algorithms Computing Models / 3 Compexity Analysis / Step 11."""

k = int(input())
m = int(input())
a = int(input())
b = int(input())

count_k = b // k - (a - 1) // k
count_m = b // m - (a - 1) // m

print(count_k - count_m)
