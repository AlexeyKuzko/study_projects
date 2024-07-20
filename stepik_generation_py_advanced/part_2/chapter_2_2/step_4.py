input_string = input()
numbers = [int(i) for i in input_string.split()]
if numbers:
    last_element = numbers.pop(-1)
    numbers.insert(0, last_element)
print(" ".join(map(str, numbers)))
