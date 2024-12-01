timur_choice = input().strip()
ruslan_choice = input().strip()

rules = {
    "камень": {"ножницы": "Тимур", "бумага": "Руслан"},
    "ножницы": {"бумага": "Тимур", "камень": "Руслан"},
    "бумага": {"камень": "Тимур", "ножницы": "Руслан"},
}

if timur_choice == ruslan_choice:
    print("ничья")
else:
    print(rules[timur_choice][ruslan_choice])
