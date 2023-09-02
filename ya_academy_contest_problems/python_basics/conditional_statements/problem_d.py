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
