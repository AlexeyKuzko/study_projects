# Функция для извлечения индексов гласных букв в слове
def extract_vowel_indices(word, vowels):
    return [i for i, ch in enumerate(word) if ch in vowels]


# Считываем входные данные
import sys

input = sys.stdin.read
data = input().split()
target_word = data[0]
n = int(data[1])
words = data[2 : 2 + n]

# Определяем множество гласных букв
vowels = set("ауоыиэяюёе")

# Получаем индексы гласных в целевом слове
target_indices = extract_vowel_indices(target_word, vowels)

# Находим и выводим слова с таким же расположением гласных
for word in words:
    word_indices = extract_vowel_indices(word, vowels)
    if word_indices == target_indices:
        print(word)
