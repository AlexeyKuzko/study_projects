number = input("")
digits_asc = sorted(number)
digits_desc = sorted(number, reverse=True)
min_number = "".join(digits_asc[0:2])
if int(min_number[0]) == 0:
    min_number = int(f'{"".join(digits_asc[1])}0')
max_number = int("".join(digits_desc[0:2]))
print(min_number, max_number)
