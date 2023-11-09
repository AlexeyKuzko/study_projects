# 1

print("Hello, World!")

# 2

# You know nothing, Jon Snow!

# 3

print("Robert")
print("Stannis")
print("Renly")

# 4

print("9780262531962")

# 5

print("What Is Dead May Never Die")

# 6

print(81 / 9)

# 7

print(6 - -81)

# 8

print(3**5)
print(-8 / -4)

# 9

print(((8 / 2) + 5) - (-3 / 2))

# 10

print(70 * (3 + 4) / (8 + 2))

# 11

print(0.39 * 0.22)

# 12

print((5**2) - (3 * 7))

# 13

print('"Khal Drogo\'s favorite word is "athjahakar""')

# 14

print('- Did Joffrey agree?\n- He did. He also said "I love using \\n".')

# 15

print("Winter " + "came " + "for " + "the " + "House " + "of " + "Frey.")

# 16

print(chr(126))
print(chr(94))
print(chr(37))

# 17

motto = "What Is Dead May Never Die!"
print(motto)

# 18

name = "Brienna"
# BEGIN
name = "anneirB"
# END
print(name)

# 19

my_brothers_count = 2
print(my_brothers_count)

# 20

family = "Targaryen"
# BEGIN
pet = "Dragon"
# END
print(family)
print(" and ")
print(pet)

# 21

euros_count = 100
# BEGIN
dollars_count = euros_count * 1.25
print(dollars_count)
yuans_count = dollars_count * 6.91
print(yuans_count)
# END

# 22

info = "We couldn't verify your mother's maiden name."
intro = "Here is important information about your account security."
first_name = "Joffrey"
greeting = "Hello"
# BEGIN
print(greeting + ", " + first_name + "!")
print(intro + "\n" + info)
# END

# 23

first_number = 20
second_number = -100
print(first_number * second_number)

# 24

king = "Rooms in King Balon's Castle:"
# BEGIN
number_of_castles = 6
rooms_per_castle = 17
print(king)
print(number_of_castles * rooms_per_castle)
# END

# 25

DRAGONS_BORN_COUNT = 3

# 26

stark = "Arya"
# BEGIN
print(f"Do you want to eat, {stark}?")
# END

# 27

name = "Na\nharis"
# BEGIN
print(name[7])
# END

# 28

value = "Hexlet"
# BEGIN
print(value[2:5])
# END

# 29

# BEGIN
text = """Lannister, Targaryen, Baratheon, Stark, Tyrell...
they're all just spokes on a wheel.
This one's on top, then that one's on top, and on and on it spins,
crushing those on the ground."""
# END
print(text)

# 30

print(-0.304)

# 31

print(7 - (-8 - -2))

# 32

one = "Naharis"
two = "Mormont"
three = "Sand"
# BEGIN
print(f"{one[2]}{two[1]}{three[3]}{two[4]}{two[2]}")
# END

# 33

value = 2.9
# BEGIN
int_value = int(value)
str_value = str(int_value)
print(str_value + " times")
# END

# 34

company1 = "Apple"
company2 = "Samsung"
# BEGIN
company1_len = len(company1)
company2_len = len(company2)
print(company1_len + company2_len)
# END

# 35

number = 255
# BEGIN
print(hex(number))
# END

# 36

number = 10.1234
# BEGIN
print(round(number, 2))
# END

# 37

text = "Never forget what you are, for surely the world will not"
# BEGIN
result = f"First: {text[0]}\nLast: {text[-1]}"
print(result)
# END

# 38

# BEGIN
print(min(3, -3, 10, 22, 0))
# END

# 39

# imports are studied on Hexlet
from random import random

# BEGIN
print(round(random() * 10))
# END

# 40

motto = "Family, Duty, Honor"
# BEGIN
print(type(motto))
# END

# 41

text = "a MIND needs Books as a Sword needS a WHETSTONE."
# BEGIN
lower_text = text.lower()
print(lower_text)
# END

# 42

first_name = "  Grigor   \n"
# BEGIN
first_name = first_name.strip()
print(first_name)
# END

# 43

text = "Never forget what you are, for surely the world will not"
# BEGIN
print(f"Index Of N: {text.find('N')}\nIndex Of ,: {text.find(',')}")
# END

# 44

text = "When \t\n you play a \t\n game of thrones you win or you die."
# BEGIN
print(len(text[4:15].strip()))
# END

# 45


def print_motto():
    print("Winter is coming")


# 46


# BEGIN
def say_hurray_three_times():
    word = "hurray!"
    return f"{word} {word} {word}"


# END

# 47


def truncate(text, length):
    # BEGIN
    result = f"{text[0:length]}..."
    return result
    # END


# 48


def get_hidden_card(card_number, stars_count=4):
    visible_digits_line = card_number[-4:]
    return f"{'*' * stars_count}{visible_digits_line}"


# 49


def trim_and_repeat(text, offset=0, repetitions=1):
    return f"{text[offset:] * repetitions}"


# 50
def word_multiply(string: str, count: int) -> str:
    return string * count


# 51


def is_pensioner(age):
    return age >= 60


# 52


def is_mister(string):
    return string == "Mister"


# 53


def is_international_phone(phone):
    return phone[0] == "+"


# 54


def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


# 55


def is_palindrome(word):
    lower_word = word.lower()
    return lower_word == lower_word[::-1]


def is_not_palindrome(word):
    return not is_palindrome(word)


# 56
def string_or_not(value):
    return isinstance(value, str) and "yes" or "no"


# 57
def guess_number(guess):
    if guess == 42:
        return "You win!"
    return "Try again!"


# 58
def normalize_url(url):
    prefix = "https://"
    if url[:8] == prefix:
        return url
    else:
        if url[:7] == "http://":
            return prefix + url[7:]
        else:
            return prefix + url


# 59
def who_is_this_house_to_starks(house_name):
    if house_name == "Karstark" or house_name == "Tully":
        return "friend"
    elif house_name == "Lannister" or house_name == "Frey":
        return "enemy"
    return "neutral"


# 60
def flip_flop(arg):
    return "flop" if arg == "flip" else "flip"


# 61


def get_number_explanation(number: int) -> str:
    match number:
        case 666:
            return "devil number"
        case 42:
            return "answer for everything"
        case 7:
            return "prime number"
        case _:
            return "just a number"


# 62


def print_numbers(last_number):
    i = last_number
    while i > 0:
        print(i)
        i = i - 1
    print("finished!")


# 63


def multiply_numbers_from_range(start, finish):
    i = start
    result = 1
    while i <= finish:
        result = result * i
        i = i + 1
    return result


# 64


def join_numbers_from_range(start, end):
    i = start
    result = ""
    while i <= end:
        result = result + str(i)
        i = i + 1
    return result


# 65


def print_reversed_word_by_symbol(word):
    i = len(word) - 1
    while i >= 0:
        print(word[i])
        i = i - 1


# 66


def count_chars(string, char):
    index = 0
    count = 0
    while index < len(string):
        if string[index].upper() == char.upper():
            count = count + 1
        index = index + 1
    return count


# 67


def my_substr(string, length):
    result_string = ""
    index = 0
    while index < length:
        result_string = result_string + string[index]
        index = index + 1

    return result_string


# 68


def is_arguments_for_substr_correct(string, index, length):
    if index < 0:
        return False
    elif length < 0:
        return False
    elif index > len(string) - 1:
        return False
    elif index + length > len(string):
        return False
    return True


# 69


def filter_string(text, char):
    index = 0
    result = ""
    while index < len(text):
        current_char = text[index]
        if current_char != char:
            result = f"{result}{current_char}"
        index += 1
    return result


# 70


def is_contains_char(string, char):
    index = 0
    while index < len(string):
        if string[index] == char:
            return True
        index += 1
    return False


# 71


def filter_string(text, char):
    result = ""
    for current_char in text:
        if current_char.upper() != char.upper():
            result += current_char
    return result
