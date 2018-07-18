import card
import random

class Deck(object):
    def __init__(self, seed):
        self.cards = []
        self.seed = seed
        for i in range(0,9):
            self.cards.append(card.Card(i))
        for i in range(0,9):
            self.cards.append(card.Card(i))
        random.shuffle(self.cards, random=self.rand)

    def rand(self):
        return self.seed

