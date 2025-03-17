number = input()

if len(number) == 6:
    print(number[0] + number[:0:-1])
else:
    print(int(number[::-1]))
