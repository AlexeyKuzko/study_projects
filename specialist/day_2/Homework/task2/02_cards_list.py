from card import Card, VALUES

# TODO-1: добавьте в список hearts_cards все червовые карты(от 2-ки до туза)
hearts_cards = []
for value in VALUES:
    hearts_cards.append(Card(value, "Hearts"))
print(f"Задание 1, отсортированный по возрастанию список объектов черновых карт.\n{hearts_cards}\n")

# TODO-2: добавьте в список diamonds_cards все бубновые карты(от туза до 2-ки)
diamonds_cards = []
for value in VALUES[::-1]:
    diamonds_cards.append(Card(value, "Diamonds"))
print(f"Задание 2, отсортированный по убыванию список объектов бубновых карт.\n{diamonds_cards}\n")

# TODO-3: выведите все карты из списка hearts_cards в терминал через запятую в одну строку:
# Пример вывода: 2♥, 3♥, 4♥ ... A♥
hearts_cards_str = ""
for card_obj in hearts_cards:
    hearts_cards_str += card_obj.to_str() + ", "
print(f"Задание 3, список черновых карт через запятую в одну строку:\n{hearts_cards_str[:-2]}")

diamonds_cards_str = ", ".join([card.to_str() for card in diamonds_cards])
print(f"И для списка бубновых карт:\n{diamonds_cards_str}")
