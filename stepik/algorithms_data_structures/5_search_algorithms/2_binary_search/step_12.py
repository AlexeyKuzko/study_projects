"""Solution for Stepik course solutions: Algorithms Data Structures / 5 Search Algorithms / 2 Binary Search / Step 12."""

import sys

input = sys.stdin.readline
n = int(input())
s = input()

L, R = -1, n
while R - L > 1:
    M = (L + R) // 2
    if s[M] == "0":
        L = M
    else:
        R = M

print(L, R)
