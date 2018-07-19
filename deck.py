import card
import random
from sklearn.model_selection import train_test_split

class Deck(object):
    def __init__(self, seed):
        self.cards = []
        self.seed = seed
        for i in range(0,9):
            self.cards.append(card.Card(i))
        for i in range(0,9):
            self.cards.append(card.Card(i))
        self.cards,_,_,_= train_test_split(self.cards, self.cards, test_size=0, random_state=int(seed))