from dataclasses import dataclass, field
from typing import List
from heapq import heappop, heappush, nsmallest, nlargest

bites: List[int] = [283, 282, 281, 263, 255, 230, 216, 204, 197, 196, 195]
names: List[str] = [
    "snow",
    "natalia",
    "alex",
    "maquina",
    "maria",
    "tim",
    "kenneth",
    "fred",
    "james",
    "sara",
    "sam",
]


@dataclass(order=True)
class Ninja:
    """
    The Ninja class will have the following features:

    string: name
    integer: bites
    support <, >, and ==, based on bites
    print out in the following format: [469] bob
    """
    name: str = field(compare=False)
    bites: int = field()

    def __str__(self) -> str:
        return f'[{self.bites}] {self.name}'

@dataclass
class Rankings:
    """
    The Rankings class will have the following features:

    method: add() that adds a Ninja object to the rankings
    method: dump() that removes/dumps the lowest ranking Ninja from Rankings
    method: highest() returns the highest ranking Ninja, but it takes an optional
            count parameter indicating how many of the highest ranking Ninjas to return
    method: lowest(), the same as highest but returns the lowest ranking Ninjas, also
            supports an optional count parameter
    returns how many Ninjas are in Rankings when len() is called on it
    method: pair_up(), pairs up study partners, takes an optional count
            parameter indicating how many Ninjas to pair up
    returns List containing tuples of the paired up Ninja objects
    """

    ninjas: list = field(default_factory=list)

    def add(self, ninja):
        heappush(self.ninjas, ninja)

    def __len__(self):
        print(self.ninjas)
        return len(self.ninjas)
    
    def dump(self):
        return heappop(self.ninjas)

    def highest(self, n = 1):
        return nlargest(n, self.ninjas)

    def lowest(self, n = 1):
        return nsmallest(n, self.ninjas)

    def pair_up(self, n: int = 3):
        return [(h, l) for h, l in zip(nlargest(n, self.ninjas), nsmallest(n, self.ninjas))]