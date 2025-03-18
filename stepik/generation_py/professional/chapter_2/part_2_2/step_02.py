# Define sets of English and Russian letters
english_letters = set("AaBCcEeHKMOoPpTXxy")
russian_letters = set("АаВСсЕеНКМОоРрТХху")

# Read input values
letter1 = input().strip()
letter2 = input().strip()
letter3 = input().strip()

# Determine the language of each letter
is_english = all(letter in english_letters for letter in [letter1, letter2, letter3])
is_russian = all(letter in russian_letters for letter in [letter1, letter2, letter3])

# Print the result based on the letters' languages
if is_russian:
    print("ru")
elif is_english:
    print("en")
else:
    print("mix")
