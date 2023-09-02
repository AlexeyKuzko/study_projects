petya = int(input(""))
vasya = int(input(""))
tolya = int(input(""))
if petya > vasya and petya > tolya:
    print("Петя")
elif tolya > vasya and petya < tolya:
    print("Толя")
else:
    print("Вася")
