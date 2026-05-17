"""Solution for Yandex Praktikum Automation QA projects: Sprint 1 Python Basics / task 3."""

world_champions = {
    2002: "Бразилия",
    2006: "Италия",
    2010: "Испания",
    2014: "Германия",
    2018: "Франция",
}

world_champions[2022] = "Аргентина"

for year, country in world_champions.items():
    print(f"{year} - {country}")

country = "Италия"
if country in world_champions.values():
    print("Италия cтановилась чемпионом мира по футболу в 21 веке!")
else:
    print("Италия не выигрывала чемпионат мира по футболу в 21 веке.")
