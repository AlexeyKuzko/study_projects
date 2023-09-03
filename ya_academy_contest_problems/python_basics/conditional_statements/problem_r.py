side1 = int(input(""))
side2 = int(input(""))
side3 = int(input(""))

if (
    side1**2 + side2**2 == side3**2
    or side1**2 + side3**2 == side2**2
    or side2**2 + side3**2 == side1**2
):
    print("100%")
elif (
    side1**2 + side2**2 < side3**2
    or side1**2 + side3**2 < side2**2
    or side2**2 + side3**2 < side1**2
):
    print("велика")
else:
    print("крайне мала")
