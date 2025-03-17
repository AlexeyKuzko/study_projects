def index_of_nearest(numbers, number):
    if not numbers:
        return -1

    min_diff = float('inf')
    min_index = -1

    for i, num in enumerate(numbers):
        diff = abs(num - number)
        if diff < min_diff or (diff == min_diff and i < min_index):
            min_diff = diff
            min_index = i

    return min_index