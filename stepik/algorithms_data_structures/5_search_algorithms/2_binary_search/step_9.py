"""Solution for Stepik course solutions: Algorithms Data Structures / 5 Search Algorithms / 2 Binary Search / Step 9."""

import sys
import bisect

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()  # На случай, если массив не отсортирован
q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    left_idx = bisect.bisect_left(a, l)
    right_idx = bisect.bisect_right(a, r)
    print(right_idx - left_idx)
