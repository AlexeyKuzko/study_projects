n = int(input().strip())
numbers = []

for _ in range(n):
    numbers.append(int(input().strip()))
target = int(input().strip())
found = False

for i in range(n):
    for j in range(n):
        if i != j and numbers[i] * numbers[j] == target:
            found = True
            break
    if found:
        break

if found:
    print("ДА")
else:
    print("НЕТ")
