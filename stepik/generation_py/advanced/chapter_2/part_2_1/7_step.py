"""Solution for Stepik course solutions: Generation Py / Advanced / Chapter 2 / Part 2 1 / 7 Step."""

number = input()

if len(number) == 6:
    print(number[0] + number[:0:-1])
else:
    print(int(number[::-1]))
