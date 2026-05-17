"""Solution for Stepik course solutions: Generation Py / Professional / Chapter 4 / Part 4 1 / Step 10."""

while True:
    try:
        line = input()
        print(line[::-1])
    except EOFError:
        break
