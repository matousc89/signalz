"""
.. versionadded:: 0.8

This function deal cards from a defined deck.

This function has different implementation if the numpy is not avilable.

Example Usage
===============

Deal five cards:

.. code-block:: python

    cards = signalz.card_dealer(5)

Deal two cards for 3 players (array with dimmension 3x2):

.. code-block:: python

    cards = signalz.card_dealer(2, players=3)

Add 2 wild cards to the deck and build deck from two such a decks:

.. code-block:: python

    cards = signalz.card_dealer(2, deck="standard+wild", decks_number=2)

You can also provide a custom deck:

.. code-block:: python

    my_deck = ["A1", "A2", "B1", "B2"]
    cards = signalz.card_dealer(2, deck=my_deck)

Function Documentation
======================================
"""
from random import shuffle

try:
    import numpy as np
except:
    pass


STANDARD_DECK = [
    "Ah", "Kh", "Qh", "Jh", "Th", "9h", "8h", "7h", "6h", "5h", "4h", "3h", "2h",
    "Ac", "Kc", "Qc", "Jc", "Tc", "9c", "8c", "7c", "6c", "5c", "4c", "3c", "2c",
    "Ad", "Kd", "Qd", "Jd", "Td", "9d", "8d", "7d", "6d", "5d", "4d", "3d", "2d",
    "As", "Ks", "Qs", "Js", "Ts", "9s", "8s", "7s", "6s", "5s", "4s", "3s", "2s"
]

DECKS = {
    "standard": STANDARD_DECK,
    "standard+wild": STANDARD_DECK + ["w", "w"],
}


def card_dealer(cards_dealt, players=1, deck="standard", decks_number=1):
    """
    This function return randomly dealt cards for defined number of players.

    Args:
    * `cards_dealt` : number of cards for each player (int)
    * `players` : number of players

    Kwargs:
    * `deck` : options are:
        * `standard` (str) - standard playging deck with 52 cards
        * `standard+wild` (str) - standard playing deck extended with two wildcards (w1, w2)
        * any list/tuple obtaining strings representing custom cards
    * `deck_number` : number of decks from which are cards dealt (some rummy games use more than one)

    Returns:
    * list of lists - list cointains list of holdings for each player
    """
    if type(deck) is str:
        try:
            deck = (DECKS[deck])
        except:
            raise Exception('Provided deck name is not known.')
    deck_to_deal = deck * decks_number
    shuffle(deck_to_deal)
    return [deck_to_deal[i:i + cards_dealt] for i in range(0, cards_dealt * players, cards_dealt)]


def card_dealer_numpy(cards_dealt, players=1, deck="standard", decks_number=1):
    """
    This function return randomly dealt cards for defined number of players.

    Args:
    * `cards_dealt` : number of cards for each player (int)
    * `players` : number of players

    Kwargs:
    * `deck` : options are:
        * `standard` (str) - standard playging deck with 52 cards
        * `standard+wild` (str) - standard playing deck extended with two wildcards (w1, w2)
        * any list/tuple obtaining strings representing custom cards
    * `deck_number` : number of decks from which are cards dealt (some rummy games use more than one)

    Returns:
    * numpy 2d array - every row represents one player
    """
    if type(deck) is str:
        try:
            deck_cards = np.array(DECKS[deck])
        except:
            raise Exception('Provided deck name is not known.')
    else:        
        try:
            deck_cards = np.array(deck)
        except:
            raise Exception('Provided deck cannot be converted to numpy array')
    cards = np.tile(deck_cards, decks_number)
    idxs = np.random.choice(len(cards), size=players*cards_dealt, replace=False)
    return np.reshape(cards[idxs], (players, cards_dealt))


