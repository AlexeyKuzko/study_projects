"""Solution for Stepik course solutions: Generation Py / Professional / Chapter 2 / Part 2 1 / Step 15."""

from functools import cmp_to_key


def compare(x, y):
    if x + y > y + x:
        return -1
    elif x + y < y + x:
        return 1
    else:
        return 0


def get_biggest(numbers):
    if not numbers:
        return -1
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(compare))
    return int("".join(numbers))
