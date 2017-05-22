#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_hight(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


def main():
    beer_card = Card('7', 'diamonds')
    print(beer_card)
    deck = FrenchDeck()

    print(len(deck))

    for i in range(len(deck)):
        print(deck[i])

    for card in deck:
        print(card)

    print('=========Reversed deck=========')
    for card in reversed(deck):
        print(card)
    print('=========Random   deck=========')
    print('Random choice deck:', choice(deck))
    print('Random choice deck:', choice(deck))

    print('=========Sorted   deck=========')
    for card in sorted(deck, key=spades_hight):
        print(card)


if __name__ == '__main__':
    main()
