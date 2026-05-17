"""Solution for Stepik course solutions: Generation Py / Advanced / Chapter 2 / Part 2 2 / Step 2."""

numbers = list(map(int, input().split()))

count = 0

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        count += 1

print(count)
