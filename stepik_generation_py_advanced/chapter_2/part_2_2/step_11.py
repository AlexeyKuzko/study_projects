input_word = input().strip()

initial_text = input_word + " запретил букву"


def remove_letter_and_cleanup(text, letter):
    new_text = text.replace(letter, "")
    return " ".join(new_text.split())


unique_letters = sorted(set(initial_text))

for letter in unique_letters:
    if letter != " ":
        print(initial_text, letter)
        initial_text = remove_letter_and_cleanup(initial_text, letter)
