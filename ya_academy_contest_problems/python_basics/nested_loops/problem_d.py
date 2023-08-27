N = int(input(""))
total_sum = 0
for i in range(N):
    num = int(input(""))
    temp_sum = 0
    while num > 0:
        digit = num % 10
        temp_sum += digit
        num //= 10
    total_sum += temp_sum
print(total_sum)
