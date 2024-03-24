# Problem A
n = int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f'{i * j} ', end='')
    print()

# Problem B


# Problem C
# Problem D
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


# Problem E
# Problem F
# Problem G
# Problem H
# Problem I
# Problem J
def divide_orange(n):
    for a in range(1, n):
        for b in range(1, n - a):
            c = n - a - b
            if c >= 1:
                print(f"{a} {b} {c}")


segments = int(input())
print("А Б В")
divide_orange(segments)


# Problem K


# Problem L


# Problem M


# Problem N


# Problem O


# Problem P


# Problem Q


# Problem R


# Problem S


# Problem T
def sum_of_digits_in_base(number, base):
    sum_of_digits = 0
    while number > 0:
        sum_of_digits += number % base
        number //= base
    return sum_of_digits


def find_optimal_base(number):
    max_sum = 0
    optimal_base = 2
    for base in range(2, 11):
        sum_of_digits = sum_of_digits_in_base(number, base)
        if sum_of_digits > max_sum:
            max_sum = sum_of_digits
            optimal_base = base
    return optimal_base


if __name__ == "__main__":
    number = int(input())
    print(find_optimal_base(number))
