# Problem A
cry = input("")

while cry != "Три!":
    print("Режим ожидания...")
    cry = input("")
print("Ёлочка, гори!")

# Problem B
count = 0

while True:
    string = input("")
    if "зайка" in string:
        count += 1
    if string == "Приехали!":
        print(count)
        break

# Problem C
beginning = int(input(""))
end = int(input(""))

for num in range(beginning, end + 1):
    print(num, end=" ")

# Problem D
start = int(input(""))
end = int(input(""))

if start <= end:
    step = 1
else:
    step = -1

for number in range(start, end + step, step):
    print(number, end=" ")

# Problem E
total = 0
while (price := float(input())) != 0:
    if price >= 500:
        price = price * 0.9
        total += price
    else:
        total += price
print(total)

# Problem F
first_number = int(input())
second_number = int(input())

while first_number != 0 and second_number != 0:
    if first_number > second_number:
        first_number = first_number % second_number
    else:
        second_number = second_number % first_number

print(first_number + second_number)

# Problem G
a = int(input())
b = int(input())
c = a * b

while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a

print(int(c / (a + b)))

# Problem H
info = input("")
repeat = int(input(""))
for i in range(repeat):
    print(f"{info}")

# Problem I
import math

x = int(input())
print(math.factorial(x))

# Problem J
x = 0
y = 0
while (instruction := input()) != "СТОП":
    steps = int(input())
    if instruction == "СЕВЕР":
        y += steps
    if instruction == "ЮГ":
        y -= steps
    if instruction == "ВОСТОК":
        x += steps
    if instruction == "ЗАПАД":
        x -= steps
print(y, x, sep="\n")

# Problem K
n = input()
summa = 0
for i in n:
    summa += int(i)
print(summa)

# Problem L
n = input()
maximum = 0
for i in n:
    if int(i) > maximum:
        maximum = int(i)
print(maximum)

# Problem M
N = int(input())
name1 = input()
for i in range(2, N + 1):
    name = input()
    if name < name1:
        name1 = name
print(name1)

# Problem N
n = int(input())
sqrt = n ** (1 / 2)
N = int(sqrt)
count = 0
if n == 1:
    count += 1
for i in range(2, N + 1):
    if n % i == 0:
        count += 1
if count > 0:
    print("NO")
else:
    print("YES")

# Problem O
N = int(input())
count = 0
for i in range(1, N + 1):
    text = input()
    if 'зайка' in text:
        count += 1
print(count)
# Problem P
n = input()
m = n[::-1]
if n == m:
    print("YES")
else:
    print("NO")

# Problem Q
n = input()
answer = ""
for i in n:
    if int(i) % 2 != 0:
        answer += i
print(answer)

# Problem R
n = int(input())
i = 2
while n != 1:
    if n % i == 0:
        n /= i
        print(i, end=" ")
        if n != 1:
            print("*", end=" ")
    else:
        i += 1

# Problem S
max_n = 1000
min_n = 1
count = 0

while count < 10:
    count += 1
    n = (max_n + min_n) // 2
    print(n)
    answer = input()
    if answer == "Меньше":
        max_n = n - 1
    elif answer == "Больше":
        min_n = n + 1
    elif answer == "Угадал!":
        break
# Problem T
N = int(input())
h = 0
answer = -1
count = 0

for n in range(N):
    b = int(input())
    m = b // (256**2)
    r = b % (256**2) // 256
    h = (37 * (m + r + h)) % 256
    hb = b - r * 256 - m * 256**2

    if h >= 100 or h != hb:
        if count == 0:
            answer = n
            count += 1

print(answer)
