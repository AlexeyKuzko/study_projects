import random

from card import SUITS, VALUES, Card


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


deck = Deck()
deck.show()
deck.shuffle()
deck.show()
deck.draw(42)
deck.show()
