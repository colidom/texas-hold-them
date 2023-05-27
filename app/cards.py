from ast import Suite
import random

class Card:
    def __init__(self, suit : Suite,rank : Rank):
        self.__suit=suit
        self.__rank=rank

    @property
    def suit(self)->Suit:
        return self


class Deck(object):

    def __init__(self, cards=None):
        if not cards:
            self.cards = [Card(suit, rank) for suit in range(4)
            for rank in range(13)]
        else:
            self.cards = list(cards)

        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

    def peek_top_card(self):
        """Peek at the top card of the deck without removing it."""
        return self.cards[-1]

    def peek_bottom_card(self):
        """Peek at the bottom card of the deck without removing it."""
        return self.cards[0]

    def shuffle(self):
        random.shuffle


class Hand:
    def __init__(self) -> None:
        pass
