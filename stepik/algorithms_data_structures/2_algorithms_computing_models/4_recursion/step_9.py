"""Solution for Stepik course solutions: Algorithms Data Structures / 2 Algorithms Computing Models / 4 Recursion / Step 9."""


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
