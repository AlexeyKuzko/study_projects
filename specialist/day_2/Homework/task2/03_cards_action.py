from card import SUITS, VALUES, Card


cards = []
# TODO-1: в список cards добавьте ВСЕ карты всех мастей
for suits in SUITS:
    for value in VALUES:
        cards.append(Card(value, suits))

# TODO-2: Выведите карты в формате: cards[кол-во]2♠, 3♠, 4♠ ... A♠, ..., 2♦, 3♦ ... A♦, 2♥, 3♥, 4♥ ... A♥
card_str = ""
for card_obj in cards:
    card_str += card_obj.to_str() + ", "

print(f"cards[{len(cards)}]{card_str[:-2]}")
