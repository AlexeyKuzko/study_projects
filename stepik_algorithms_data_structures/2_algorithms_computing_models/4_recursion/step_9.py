def calculatePower(base, exponent):
    if exponent == 0:
        return 1
    elif exponent > 0:
        return base * calculatePower(base, exponent - 1)
    else:
        return 1 / calculatePower(base, -exponent)

base_input = input().split()
base = float(base_input[0])
exponent = int(base_input[1])

result = calculatePower(base, exponent)

print("{0:.2f}".format(result))