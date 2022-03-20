from collections import namedtuple
from datetime import datetime
from mimetypes import init

Transaction = namedtuple('Transaction', 'giver points date')
# https://twitter.com/raymondh/status/953173419486359552
Transaction.__new__.__defaults__ = (datetime.now(),)


class User:

    def __init__(self, name: str) -> None:
        self._transactions = []
        self.name: str = name

    def __add__(self, transaction: 'Transaction'):
        self._transactions.append(transaction)

    @property
    def karma(self) -> int:
        return sum(t.points for t in self._transactions)

    @property
    def points(self) -> list:
        return [t.points for t in self._transactions]

    @property
    def fans(self) -> int:
        return len({t.giver for t in self._transactions})

    def __str__(self) -> str:
        plural = 's' if self.fans > 1 else ''
        return f'{self.name} has a karma of {self.karma} and {self.fans} fan{plural}'