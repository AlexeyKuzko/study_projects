"""Solution for Specialist Python OOP course materials: Day 4 / Homework / Help For Money."""

import json
from pprint import pprint


with open("daily_json.json", encoding="utf8") as file:
    data_dict = json.load(file)

pprint(data_dict)
print(data_dict["Valute"]["EUR"]["Value"])
print(data_dict["Valute"]["USD"]["Value"])
