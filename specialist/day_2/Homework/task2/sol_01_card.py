"""Начнем с создания карты"""
# ♥ ♦ ♣ ♠
VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
SUITS = ('Spades', 'Clubs', 'Diamonds', 'Hearts')
SUITS_UNI = {
        'Spades': '♠',
        'Clubs': '♣',
        'Diamonds': '♦',
        'Hearts': '♥'
}


class Card:
    """Карты в колоде должны являться объектами - экземплярами класса Card"""
    def __init__(self, value: str, suit: str):
        """При создании конструктор карты принимает: значение карты и ее масть."""
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit    # Масть карты

    def to_str(self) -> str:
        """Метод возвращает строковое представление карты в виде строки, формата:4♦"""
        return f"{self.value}{SUITS_UNI[self.suit]}"

    def equal_suit(self, other_card) -> bool:
        return self.suit == other_card.suit

    def more(self, other_card) -> bool:
        if self.VALUES.index(self.value) > self.VALUES.index(other_card.value):
            return True
        if self.VALUES.index(self.value) < self.VALUES.index(other_card.value):
            return False
        return self.SUITS.index(self.suit) > self.SUITS.index(other_card.suit)

    def less(self,other_card) -> bool:
        if self.VALUES.index(self.value) < self.VALUES.index(other_card.value):
            return True
        if self.VALUES.index(self.value) > self.VALUES.index(other_card.value):
            return False
        return self.SUITS.index(self.suit) < self.SUITS.index(other_card.suit)


# # # Создадим несколько карт
card1 = Card("10", "Hearts")
card2 = Card("A", "Diamonds")

# Выведем карты на экран в виде: 10♥ и A♦
print(card1.to_str())
print(card2.to_str())
#
# # Проверим, одинаковые ли масти у карт
# if card1.equal_suit(card2):
#     print(f"У карт: {card1.to_str()} и {card2.to_str()} одинаковые масти")
# else:
#     print(f"У карт: {card1.to_str()} и {card2.to_str()} разные масти")

print('\u2661', '\u2665')
print('\u2662', '\u2666')
print('\u2667', '\u2663')
print('\u2664', '\u2660')
