import sys

input = sys.stdin.readline
n = int(input())  # число детей
names = input().split()  # имена детей
left = [0] * n
right = [0] * n

for i in range(n):
    left[i] = (i - 1 + n) % n
    right[i] = (i + 1) % n

for p in map(int, input().split()):
    person = p - 1
    print(names[left[person]], names[right[person]])
    l = left[person]
    r = right[person]
    left[r] = l
    right[l] = r
