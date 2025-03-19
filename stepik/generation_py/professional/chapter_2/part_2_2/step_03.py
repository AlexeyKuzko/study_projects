# Read input values
n, X, Y, A, B = map(int, input().split())

# Generate the initial sequence
sequence = list(range(1, n + 1))

# Reverse the part from X to Y
sequence[X - 1 : Y] = reversed(sequence[X - 1 : Y])

# Reverse the part from A to B
sequence[A - 1 : B] = reversed(sequence[A - 1 : B])

# Print the result
print(*sequence)
