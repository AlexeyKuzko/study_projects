total = 0
while (price := float(input())) != 0:
    if price >= 500:
        price = price * 0.9
        total += price
    else:
        total += price
print(total)
