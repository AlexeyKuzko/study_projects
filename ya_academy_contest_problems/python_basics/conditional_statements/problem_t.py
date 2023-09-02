string_1 = str(input())
string_2 = str(input())
string_3 = str(input())
if "зайка" in string_1 and "зайка" not in string_2 and "зайка" not in string_3:
    print(string_1, len(string_1))
elif "зайка" in string_2 and "зайка" not in string_1 and "зайка" not in string_3:
    print(string_2, len(string_2))
elif "зайка" in string_3 and "зайка" not in string_1 and "зайка" not in string_2:
    print(string_3, len(string_3))
elif "зайка" in string_1 and "зайка" in string_2 and "зайка" not in string_3:
    output = min(string_1, string_2)
    print(f"{output} {len(output)}")
elif "зайка" in string_1 and "зайка" in string_3 and "зайка" not in string_2:
    output = min(string_1, string_3)
    print(f"{output} {len(output)}")
elif "зайка" in string_2 and "зайка" in string_3 and "зайка" not in string_1:
    output = min(string_2, string_3)
    print(f"{output} {len(output)}")
elif "зайка" in string_1 and "зайка" in string_2 and "зайка" in string_3:
    output = min(string_1, string_2, string_3)
    print(f"{output} {len(output)}")
