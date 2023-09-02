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
