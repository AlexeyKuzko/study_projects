# Read the number of people
n = int(input())

# Read the languages known by each person
languages_list = [set(input().split(", ")) for _ in range(n)]

# Find the intersection of all sets
common_languages = set.intersection(*languages_list)

# Print the result
if common_languages:
    print(", ".join(sorted(common_languages)))
else:
    print("Сериал снять не удастся")
