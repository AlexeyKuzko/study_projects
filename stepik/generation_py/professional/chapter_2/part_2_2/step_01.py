# Read input values
d1 = int(input())
d2 = int(input())
d3 = int(input())

# Calculate the minimum distance
min_distance = min(d1 + d2 + d3, 2 * (d1 + d2), 2 * (d1 + d3), 2 * (d2 + d3))

# Print the result
print(min_distance)
