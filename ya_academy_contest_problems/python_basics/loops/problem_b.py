count = 0

while True:
    string = input("")
    if "зайка" in string:
        count += 1
    if string == "Приехали!":
        print(count)
        break
