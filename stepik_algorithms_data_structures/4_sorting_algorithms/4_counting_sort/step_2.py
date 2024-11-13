n = int(input())
a = list(map(int, input().split()))

count = [0] * 15001
for mark in a:
    count[mark] += 1


missing = sum(1 for x in count[1:] if x == 0)
print(missing)
