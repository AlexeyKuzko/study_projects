"""Solution for Stepik course solutions: Generation Py / Advanced / Chapter 4 / Part 4 2 / Step 16."""

list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]

# Flatten the list
flat_list = [element for sublist in list1 for element in sublist]

# Calculate the sum of all numbers
total_sum = sum(flat_list)

# Calculate the total count of numbers
total_count = len(flat_list)

# Calculate the average
average = total_sum / total_count

print(average)
