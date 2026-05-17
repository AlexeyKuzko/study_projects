"""Solution for Stepik course solutions: Generation Py / Professional / Chapter 2 / Part 2 1 / Step 07."""


def is_valid(string):
    return len(string) in {4, 5, 6} and all(c in "0123456789" for c in string)
