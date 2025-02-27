def hide_card(card_number):
    # Убираем все пробелы из строки
    cleaned_card_number = ''.join(card_number.split())
    # Заменяем первые 12 цифр на *
    return '*' * 12 + cleaned_card_number[-4:]
