timur_choice = input().strip()
ruslan_choice = input().strip()

rules = {
    "камень": {"ножницы": "Тимур", "ящерица": "Тимур", "бумага": "Руслан", "Спок": "Руслан"},
    "ножницы": {"бумага": "Тимур", "ящерица": "Тимур", "камень": "Руслан", "Спок": "Руслан"},
    "бумага": {"камень": "Тимур", "Спок": "Тимур", "ножницы": "Руслан", "ящерица": "Руслан"},
    "ящерица": {"Спок": "Тимур", "бумага": "Тимур", "камень": "Руслан", "ножницы": "Руслан"},
    "Спок": {"ножницы": "Тимур", "камень": "Тимур", "бумага": "Руслан", "ящерица": "Руслан"}
}

if timur_choice == ruslan_choice:
    print("ничья")
else:
    print(rules[timur_choice][ruslan_choice])