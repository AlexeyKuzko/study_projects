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
