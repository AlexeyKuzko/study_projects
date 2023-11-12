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
