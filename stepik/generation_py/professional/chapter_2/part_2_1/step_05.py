"""Solution for Stepik course solutions: Generation Py / Professional / Chapter 2 / Part 2 1 / Step 05."""


def hide_card(card_number):
    # Убираем все пробелы из строки
    cleaned_card_number = "".join(card_number.split())
    # Заменяем первые 12 цифр на *
    return "*" * 12 + cleaned_card_number[-4:]
