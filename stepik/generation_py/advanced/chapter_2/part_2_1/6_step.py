"""Solution for Stepik course solutions: Generation Py / Advanced / Chapter 2 / Part 2 1 / 6 Step."""

year = int(input())
animals = ["Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц", "Дракон", "Змея", "Лошадь", "Овца"]
print(animals[year % 12])
