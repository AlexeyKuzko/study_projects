username = input("Как Вас зовут?")
print(
    f"""
Здравствуйте, {username}!"""
)
dela = str(input("Как дела?"))
if dela == "хорошо":
    print(
        f"""
Я за вас рада!"""
    )
elif dela == "плохо":
    print(
        f"""
Всё наладится!"""
    )
