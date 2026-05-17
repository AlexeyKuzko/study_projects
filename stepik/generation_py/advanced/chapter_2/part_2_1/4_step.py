"""Solution for Stepik course solutions: Generation Py / Advanced / Chapter 2 / Part 2 1 / 4 Step."""

input_string = str(input(""))

cost_per_character = 0.6
total_cost = len(input_string) * cost_per_character

rubles = int(total_cost)
kopecks = round((total_cost - rubles) * 100)

print(f"{rubles} р. {kopecks} коп.")
