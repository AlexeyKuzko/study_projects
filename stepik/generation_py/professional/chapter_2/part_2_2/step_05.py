# Read input value
n = int(input())


# Function to calculate the sum of digits of a number
def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))


# Dictionary to store groups by sum of digits
groups = {}

# Group numbers by the sum of their digits
for i in range(1, n + 1):
    digit_sum = sum_of_digits(i)
    if digit_sum in groups:
        groups[digit_sum].append(i)
    else:
        groups[digit_sum] = [i]

# Find the maximum group length
max_group_length = max(len(group) for group in groups.values())

# Print the result
print(max_group_length)
