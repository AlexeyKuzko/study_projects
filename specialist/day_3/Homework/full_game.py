"""Создадим консольную игру “Дурака без козырей”"""
import random

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
        self.suit = suit  # Масть карты

    def __str__(self):
        return self.to_str()

    def __lt__(self, other):
        return (VALUES.index(self.value), SUITS.index(self.suit)) < (VALUES.index(other.value),SUITS.index(other.suit))

    def to_str(self) -> str:
        """Метод возвращает строковое представление карты в виде строки, формата:4♦"""
        return f"{self.value}{SUITS_UNI[self.suit]}"

    def equal_suit(self, other_card) -> bool:
        """Метод проверяет, одинаковые ли масти у карт"""
        return self.suit == other_card.suit

    def more(self, other_card) -> bool:
        """Возвращает True, если карта у которой вызван метод больше,
        чем карта, которую передали в качестве параметра"""
        return ((VALUES.index(self.value), SUITS.index(self.suit)) >
                (VALUES.index(other_card.value), SUITS.index(other_card.suit)))

    def less(self, other_card) -> bool:
        """Метод проверяет, является ли карта младше, чем карта в параметре"""
        return not self.more(other_card)


class Deck:
    """Колода состоит из 52 карт (объектов класса Card)"""

    def __init__(self):
        """При создании новой колоды все карты должны находиться в отсортированном порядке -
        сначала идут все пики от 2-ки до туза, затем крести, буби и червы."""
        self.cards = []
        for suits in SUITS:
            for value in VALUES:
                self.cards.append(Card(value, suits))

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        return ", ".join(card.to_str() for card in self.cards)

    def shuffle(self):
        """Метод перемешивает колоду, располагая карты в случайном порядке"""
        random.shuffle(self.cards)

    def draw(self, x: int):
        """Возвращает x первых карт из колоды в виде списка, эти карты убираются из колоды.
        Уточнение: первую карту в списке считаем верхней картой колоды"""
        draw_x = self.cards[:x]
        self.cards = self.cards[x:]
        return draw_x

    def show(self):
        """Отображает все карты колоды в формате:
        deck[12]: 3♥, 4♦, A♣, …
        где 12 - текущее кол-во карт в колоде"""
        print(f"deck[{len(self.cards)}]: {self}")


class Player:
    def __init__(self, name: str, cards: list[Card]):
        self.name = name
        self.hand = cards

    def sort_hand(self):
        """Сортировка карт по старшинству"""
        self.hand.sort()

    def show_hand(self):
        return ", ".join(str(card) for card in self.hand)

    def has_cards(self) -> bool:
        return len(self.hand) > 0

    def take_cards(self, cards: list[Card]):
        self.hand.extend(cards)
        self.sort_hand()

    def remove_card(self, card: Card):
        self.hand.remove(card)

    def get_lowest_card(self) -> Card:
        """Самая маленькая карта"""
        self.sort_hand()
        return self.hand[0]

    def try_beat(self, attack_card: Card) -> Card | None:
        possible = [
            card for card in self.hand
            if card.equal_suit(attack_card) and card.more(attack_card)
        ]

        if not possible:
            return None

        # найдём минимальную вручную через less
        min_card = possible[0]
        for card in possible[1:]:
            if card.less(min_card):
                min_card = card

        return min_card

    def refill_from_deck(self, deck: Deck, limit: int = 10):
        """Добор карт до 10"""
        while len(self.hand) < limit and deck.cards:
            self.hand.append(deck.draw(1)[0])
        self.sort_hand()


deck = Deck()
deck.shuffle()

player1 = Player("Игрок-1", deck.draw(10))
player2 = Player("Игрок-2", deck.draw(10))

attacker = player1
defender = player2

table = []


# --- Игровой цикл ---

while player1.has_cards() and player2.has_cards():

    print(f"\nХодит {attacker.name}")
    print(f"{attacker.name}: {attacker.show_hand()}")
    print(f"{defender.name}: {defender.show_hand()}")

    # 1. Атакующий кладёт самую маленькую карту
    attack_card = attacker.get_lowest_card()
    attacker.remove_card(attack_card)
    table = [attack_card]

    print(f"{attacker.name} ходит: {attack_card}")

    # 2. Защитник пытается побить
    beat_card = defender.try_beat(attack_card)

    if beat_card is None:
        # 3. Не смог побить → забирает карты
        print(f"{defender.name} не смог побить и забирает карты")
        defender.take_cards(table)
    else:
        defender.remove_card(beat_card)
        table.append(beat_card)
        print(f"{defender.name} бьёт картой: {beat_card}")

        # 5. Если отбился — меняемся ролями
        attacker, defender = defender, attacker

    # 7. Добор карт
    attacker.refill_from_deck(deck)
    defender.refill_from_deck(deck)

    table.clear()


# --- Завершение игры ---

print("\nИгра окончена!")

if not player1.has_cards() and not player2.has_cards():
    print("Ничья!")
elif not player1.has_cards():
    print("Победил Игрок-1!")
else:
    print("Победил Игрок-2!")