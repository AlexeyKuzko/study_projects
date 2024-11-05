s = input()
balance = 0
removed = 0
for char in s:
    if char == "(":
        balance += 1
    elif balance > 0:
        balance -= 1
    else:
        removed += 1
removed += balance
print(removed)
