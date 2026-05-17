"""Solution for Stepik course solutions: Generation Py / Advanced / Chapter 2 / Part 2 2 / Step 5."""

input_data = input()
numbers = list(map(int, input_data.split()))
unique_numbers = set(numbers)
print(len(unique_numbers))
