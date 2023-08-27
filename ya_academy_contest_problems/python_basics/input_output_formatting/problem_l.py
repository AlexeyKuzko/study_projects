def sum_without_carry(num1, num2):
    results = 0
    scale = 1
    while num1 > 0 or num2 > 0:
        digit1 = num1 % 10
        digit2 = num2 % 10

        sum_digits = (digit1 + digit2) % 10
        results += sum_digits * scale

        num1 //= 10
        num2 //= 10
        scale *= 10
    return results


input1 = int(input(""))
input2 = int(input(""))
result = sum_without_carry(input1, input2)
print(result)
