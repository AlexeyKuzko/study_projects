# Problem A
username = input("Как Вас зовут?")
print(
    f"""
Здравствуйте, {username}!"""
)
dela = str(input("Как дела?"))
if dela == "хорошо":
    print(
        f"""
Я за вас рада!"""
    )
elif dela == "плохо":
    print(
        f"""
Всё наладится!"""
    )


# Problem B
petya = int(input(""))
vasya = int(input(""))
if petya > vasya:
    print("Петя")
else:
    print("Вася")


# Problem C
petya = int(input(""))
vasya = int(input(""))
tolya = int(input(""))
if petya > vasya and petya > tolya:
    print("Петя")
elif tolya > vasya and petya < tolya:
    print("Толя")
else:
    print("Вася")


# Problem D
petya = int(input(""))
vasya = int(input(""))
tolya = int(input(""))
fastest = max(petya, tolya, vasya)
if fastest == petya:
    print("1. Петя")
    if vasya > tolya:
        print("2. Вася\n3. Толя")
    else:
        print("2. Толя\n3. Вася")
elif fastest == vasya:
    print("1. Вася")
    if petya > tolya:
        print("2. Петя\n3. Толя")
    else:
        print("2. Толя\n3. Петя")
elif fastest == tolya:
    print("1. Толя")
    if petya > vasya:
        print("2. Петя\n3. Вася")
    else:
        print("2. Вася\n3. Петя")


# Problem E
petya = 7
vasya = 6
petya -= 1
vasya += 3
vasya += 3
N = int(input(""))
M = int(input(""))
petya += N
vasya += M
if petya > vasya:
    print("Петя")
else:
    print("Вася")


# Problem F
year = int(input(""))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")
else:
    print("NO")


# Problem G
number = input("")

if number == number[::-1]:
    print("YES")
else:
    print("NO")


# Problem H
string = str(input())

if "зайка" in string:
    print("YES")
else:
    print("NO")


# Problem I
str1 = input("")
str2 = input("")
str3 = input("")
less = min(str1, str2, str3)
if less == str1:
    print(str1)
elif less == str2:
    print(str2)
else:
    print(str3)


# Problem J
password = input()
sum_least_significant = int(password[1]) + int(password[2])
sum_most_significant = int(password[0]) + int(password[1])
new_number = str(max(sum_least_significant, sum_most_significant)) + str(
    min(sum_least_significant, sum_most_significant)
)

print(new_number)


# Problem K
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


# Problem L
length1 = int(input(""))
length2 = int(input(""))
length3 = int(input(""))

if (
    length1 + length2 > length3
    and length1 + length3 > length2
    and length2 + length3 > length1
):
    print("YES")
else:
    print("NO")


# Problem M
elf_number = input("")
gnome_number = input("")
human_number = input("")

common_digit = ""

for i in range(2):
    if elf_number[i] == gnome_number[i] == human_number[i]:
        common_digit = elf_number[i]
        break
print(common_digit)


# Problem N
number = input("")
digits_asc = sorted(number)
digits_desc = sorted(number, reverse=True)
min_number = "".join(digits_asc[0:2])
if int(min_number[0]) == 0:
    min_number = int(f'{"".join(digits_asc[1])}0')
max_number = int("".join(digits_desc[0:2]))
print(min_number, max_number)


# Problem O
number_1 = int(input())
number_2 = int(input())
a = number_1 // 10
b = number_1 % 10
c = number_2 // 10
d = number_2 % 10
maximum = max(a, b, c, d)
minimum = min(a, b, c, d)
total = a + b + c + d
middle = (total - minimum - maximum) % 10
print(f"{maximum}{middle}{minimum}")


# Problem P
p = int(input())
v = int(input())
t = int(input())
first = max(p, v, t)
second = 0
third = min(p, v, t)
if p != first and p != third:
    second = "Петя"
elif v != first and v != third:
    second = "Вася"
elif t != first and t != third:
    second = "Толя"
if p == first:
    first = "Петя"
elif v == first:
    first = "Вася"
elif t == first:
    first = "Толя"
if p == third:
    third = "Петя"
elif v == third:
    third = "Вася"
elif t == third:
    third = "Толя"
print(
    f"{' ' * 10}{first}{' ' * 10}\n{' ' * 2}{second}{' ' * 18}\n{' ' * 18}{third}{' ' * 2}"
)
print(f"{' ' * 3}II{' ' * 6}I{' ' * 6}III{' ' * 2}")


# Problem Q
a = float(input())
b = float(input())
c = float(input())
D = b**2 - 4 * a * c

if a == 0 and b == 0 and c == 0:
    print("Infinite solutions")
elif a == 0 and b == 0:
    print("No solution")
elif a == 0:
    x1 = -c / b
    print(f"{x1:.2f}")
elif D > 0:
    x1 = (-b - (D**0.5)) / (2 * a)
    x2 = (-b + (D**0.5)) / (2 * a)
    print(f"{min(x1, x2):.2f} {max(x1, x2):.2f}")
elif D == 0:
    x1 = -b / (2 * a)
    print(f"{x1:.2f}")
else:
    print("No solution")


# Problem R
side1 = int(input(""))
side2 = int(input(""))
side3 = int(input(""))

if (
    side1**2 + side2**2 == side3**2
    or side1**2 + side3**2 == side2**2
    or side2**2 + side3**2 == side1**2
):
    print("100%")
elif (
    side1**2 + side2**2 < side3**2
    or side1**2 + side3**2 < side2**2
    or side2**2 + side3**2 < side1**2
):
    print("велика")
else:
    print("крайне мала")


# Problem S
x = float(input())
y = float(input())
r = 10

if x**2 + y**2 > r**2:
    print("Вы вышли в море и рискуете быть съеденным акулой!")
elif x > 0 and y > 0 and x**2 + y**2 < 25:
    print("Опасность! Покиньте зону как можно скорее!")
elif x < 0 and (0 < y < 5) and y < ((5 / 3) * x + (35 / 3)):
    print("Опасность! Покиньте зону как можно скорее!")
elif y < 0 and (-7 < x < 5) and (y > ((1 / 4) * (x**2) + (x / 2) - (35 / 4))):
    print("Опасность! Покиньте зону как можно скорее!")
else:
    print("Зона безопасна. Продолжайте работу.")


# Problem T
string_1 = str(input())
string_2 = str(input())
string_3 = str(input())
if "зайка" in string_1 and "зайка" not in string_2 and "зайка" not in string_3:
    print(string_1, len(string_1))
elif "зайка" in string_2 and "зайка" not in string_1 and "зайка" not in string_3:
    print(string_2, len(string_2))
elif "зайка" in string_3 and "зайка" not in string_1 and "зайка" not in string_2:
    print(string_3, len(string_3))
elif "зайка" in string_1 and "зайка" in string_2 and "зайка" not in string_3:
    output = min(string_1, string_2)
    print(f"{output} {len(output)}")
elif "зайка" in string_1 and "зайка" in string_3 and "зайка" not in string_2:
    output = min(string_1, string_3)
    print(f"{output} {len(output)}")
elif "зайка" in string_2 and "зайка" in string_3 and "зайка" not in string_1:
    output = min(string_2, string_3)
    print(f"{output} {len(output)}")
elif "зайка" in string_1 and "зайка" in string_2 and "зайка" in string_3:
    output = min(string_1, string_2, string_3)
    print(f"{output} {len(output)}")
