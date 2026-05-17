"""Solution for Stepik course solutions: Algorithms Data Structures / 3 Basic Data Structures / 5 Stack / Step 9."""

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
