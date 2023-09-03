str1 = input("")
str2 = input("")
str3 = input("")
less = min(str1, str2, str3)
if less == str1:
    print(str1)
elif less == str2:
    print(str2)
else:
    print(str3)
