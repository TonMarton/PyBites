from collections import namedtuple, Counter
from enum import Enum
from typing import Sequence, List

Suit = Enum("Suit", list("SHDC"))
Rank = Enum("Rank", list("AKQJT98765432"))
Card = namedtuple("Card", ["suit", "rank"])

HCP = {Rank.A: 4, Rank.K: 3, Rank.Q: 2, Rank.J: 1}
SSP = {2: 1, 1: 2, 0: 3}  # cards in a suit -> short suit points


class BridgeHand:
    def __init__(self, cards: Sequence[Card]):
        """
        Process and store the sequence of Card objects passed in input.
        Raise TypeError if not a sequence
        Raise ValueError if any element of the sequence is not an instance
        of Card, or if the number of elements is not 13
        """
        if not isinstance(cards, Sequence):
            raise TypeError
        if len(cards) != 13 or not all(isinstance(card, Card) for card in cards):
            raise ValueError

        self.cards: list = sorted(list(cards), key=lambda card: (card.suit.value, card.rank.value))

    def __str__(self) -> str:
        """
        Return a string representing this hand, in the following format:
        "S:AK3 H:T987 D:KJ98 C:QJ"
        List the suits in SHDC order, and the cards within each suit in
        AKQJT..2 order.
        Separate the suit symbol from its cards with a colon, and
        the suits with a single space.
        Note that a "10" should be represented with a capital 'T'
        """ 
        hand_string = ''
        current_suit: Suit = None
        for suit, rank in self.cards:
            if current_suit != suit:
                current_suit = suit
                hand_string += ' '
                hand_string += suit.name + ':'
            hand_string += rank.name
        return hand_string.strip()



    @property
    def hcp(self) -> int:
        """ Return the number of high card points contained in this hand """
        return sum(HCP[card.rank] for card in self.cards if card.rank in HCP) 

    def _suit_count(self, req_count: int) -> int:
        counter = Counter(card.suit for card in self.cards)
        print(counter)
        return sum(1 for suit in Suit if counter[suit] == req_count)

    @property
    def doubletons(self) -> int:
        """ Return the number of doubletons contained in this hand """
        return self._suit_count(2)

    @property
    def singletons(self) -> int:
        """ Return the number of singletons contained in this hand """
        return self._suit_count(1)

    @property
    def voids(self) -> int:
        """ Return the number of voids (missing suits) contained in
            this hand
        """
        return self._suit_count(0)

    @property
    def ssp(self) -> int:
        """ Return the number of short suit points in this hand.
            Doubletons are worth one point, singletons two points,
            voids 3 points
        """
        return sum(self._suit_count(count) * points for count, points in SSP.items()) 


    @property
    def total_points(self) -> int:
        """ Return the total points (hcp and ssp) contained in this hand """
        return self.ssp + self.hcp

    @property
    def ltc(self) -> int:
        """ Return the losing trick count for this hand - see bite description
            for the procedure
        """
        counter = Counter(card.suit for card in self.cards)
        startIndex = 0
        ltc = 0
        for _, count in counter.items():
            ltc += count if count < 4 else 3
            endIndex = startIndex + count
            topThree = startIndex + 3 if endIndex > startIndex + 3 else endIndex
            for card in self.cards[startIndex:topThree]:
                
                if card.rank in [rank for rank in Rank][:topThree-startIndex]:
                    ltc -= 1
                else:
                    break
            startIndex = endIndex
        return ltc
            
            

