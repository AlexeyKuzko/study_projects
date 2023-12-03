first_number = int(input())
second_number = int(input())

while first_number != 0 and second_number != 0:
    if first_number > second_number:
        first_number = first_number % second_number
    else:
        second_number = second_number % first_number

print(first_number + second_number)
