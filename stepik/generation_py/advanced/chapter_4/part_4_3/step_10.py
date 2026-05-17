"""Solution for Stepik course solutions: Generation Py / Advanced / Chapter 4 / Part 4 3 / Step 10."""


def pascal(n):
    if n == 0:
        return [1]
    else:
        prev_row = pascal(n - 1)
        return [x + y for x, y in zip([0] + prev_row, prev_row + [0])]


n = int(input())
print(pascal(n))
