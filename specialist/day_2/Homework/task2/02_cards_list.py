from random import shuffle
from sol_01_card import Card


class Deck:
    VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    SUITS = ['♠', '♣', '♦', '♥']

    def __init__(self):
        self.cards = []
        for suit in self.SUITS:
            for value in self.VALUES:
                self.cards.append(Card(value, suit))

    def shuffle(self):
        shuffle(self.cards)

    def draw(self, x: int):
        taken = self.cards[:x]
        self.cards = self.cards[x:]
        return taken

    def show(self):
        cards_str = ", ".join(card.to_str() for card in self.cards)
        print(f"deck[{len(self.cards)}]: {cards_str}")