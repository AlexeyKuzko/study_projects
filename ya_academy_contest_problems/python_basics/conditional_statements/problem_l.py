length1 = int(input(""))
length2 = int(input(""))
length3 = int(input(""))

if (
    length1 + length2 > length3
    and length1 + length3 > length2
    and length2 + length3 > length1
):
    print("YES")
else:
    print("NO")
