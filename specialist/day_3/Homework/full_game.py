"""Создадим консольную игру “Дурака без козырей”"""
import random
# константы и классы карты\колоды перепечатаны из предыдущей работы, но можно было бы импортировать их

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
    """Класс игрока, экземплярами которого будут играющие"""

    def __init__(self, name: str, cards: list[Card]):
        """Конструктор игрока, сохраняем имя и выдаем карты на руку"""
        self.name = name
        self.hand = cards

    def _sort_hand(self):
        """Сортировка по 'старшенству' для начала игры и аккуратной визуализации"""
        self.hand.sort()

    def get_lowest_card(self) -> Card:
        """Возвращает самую маленькую карту по старшинству в начале хода"""
        self._sort_hand()
        return self.hand[0]

    def show_hand(self):
        """Метод, чтобы выводить в консоль максимально наглядную визуализацию данных ходов"""
        return ", ".join(str(card) for card in self.hand)

    def try_beat(self, attack_card: Card) -> Card | None:
        """Игрок пытается побить карту атакующего, если у него есть такая же масть, но значением больше"""
        # нужна карта той же масти, что и атакующая, но больше по номиналу
        beatable = [card for card in self.hand if card.equal_suit(attack_card) and card.more(attack_card)]
        if not beatable:
            return None
        if len(beatable) == 1:  # если есть несколько подходящих карт, берем наименьшую по номиналу
            return beatable[0]
        min_card = beatable[0]
        for card in beatable[1:]:
            if card.less(min_card):
                min_card = card
        return min_card

    def has_cards(self) -> bool:
        """Проверяем, остались ли карты на руке (если нет, вернется False и игра закончится)"""
        return len(self.hand) > 0

    def take_cards(self, cards: list[Card]):
        """Если игрок не может побить карту, то забирает ее себе в руку"""
        self.hand.extend(cards)
        self._sort_hand()

    def remove_card(self, card: Card):
        """Удаляем карту из руки (при атаке или успешной защите)"""
        self.hand.remove(card)

    def refill_from_deck(self, deck: Deck, limit: int = 10):
        """Реализовать возможность добрать карты из колоды после того, как один из игроков отбился/взял в руку"""
        while len(self.hand) < limit and deck.cards:  # пока меньше лимита руки и еще есть карты в колоде
            self.hand.append(deck.draw(1)[0])  # добавляем в руку сверху колоды (колоду уменьшаем)
        self._sort_hand()

if __name__ == "__main__":
    # Ставим стол; берем колоду и замешиваем ее; усаживаем за стол двух игроков, которые берут по 10 карт
    table = []
    deck = Deck()
    deck.shuffle()
    attacker, defender = Player("Алексей", deck.draw(10)), Player("Вадим Викторович", deck.draw(10))
    # Цикл игры идет до тех пор, пока у кого-нибудь из игроков не останется ни одной карты
    while attacker.has_cards() and defender.has_cards():
        print(f"\nАтакует игрок {attacker.name}")
        print(f"Карты атакующего ({attacker.name}): {attacker.show_hand()}")
        print(f"Карты отбивающегося ({defender.name}): {defender.show_hand()}")

        attack_card = attacker.get_lowest_card()  # атакующий выкладывает наименьшую карту с руки
        attacker.remove_card(attack_card)
        table = [attack_card]
        print(f"{attacker.name} ходит картой {attack_card}")

        beat_card = defender.try_beat(attack_card) # защищающийся пытается отбиться
        if beat_card:
            defender.remove_card(beat_card)
            table.append(beat_card)
            print(f"{defender.name} отбивается картой {beat_card}")
            attacker, defender = defender, attacker # если отбился, меняемся ролями
        else:
            print(f"{defender.name} не смог побить и забирает карты")
            defender.take_cards(table)

        attacker.refill_from_deck(deck)  # доборы на руку из колоды
        defender.refill_from_deck(deck)
        table.clear()

    print("\nИгра окончена!")
    if not attacker.has_cards() and not defender.has_cards():
        print("Ничья, победила дружба!")
    elif not attacker.has_cards():
        print(f"Победил {attacker.name}!")
    else:
        print(f"Победил {defender.name}!")
    