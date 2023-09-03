number = input("")

digit1 = int(number[0])
digit2 = int(number[1])
digit3 = int(number[2])

minimum = min(digit1, digit2, digit3)
maximum = max(digit1, digit2, digit3)

remaining = digit1 + digit2 + digit3 - minimum - maximum

if minimum + maximum == remaining * 2:
    print("YES")
else:
    print("NO")
