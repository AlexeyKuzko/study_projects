# Read input values
numbers = list(map(int, input().split()))

# Create a dictionary to count occurrences of each number
count_dict = {}
for number in numbers:
    if number in count_dict:
        count_dict[number] += 1
    else:
        count_dict[number] = 1

# Find numbers that occur more than once
repeated_numbers = [num for num, count in count_dict.items() if count > 1]

# Sort the numbers in ascending order
repeated_numbers.sort()

# Print the result
print(*repeated_numbers)
