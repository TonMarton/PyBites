from collections import deque
from functools import total_ordering

@total_ordering
class Account:

    def __init__(self, name, start_balance = 0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []

    @property
    def balance(self):
        return self.start_balance + sum(self._transactions)

    def add_transaction(self, transaction: int):
        self._transactions.append(transaction)

    # add dunder methods below
    def __len__(self):
        return len(self._transactions)

    def __lt__(self, other: 'Account'):
        return self.balance < other.balance

    def __eq__(self, other: 'Account'):
        return self.balance == other.balance
    
    def __getitem__(self, key):
        return self._transactions[key]
    
    def __add__(self, other: int):
        if type(other) != int:
            raise TypeError(f'Does not support operation between int and {type(other)}')
        self._transactions.append(other)

    def __sub__(self, other: int):
        if type(other) != int:
            raise TypeError(f'Does not support operation between int and {type(other)}')
        self._transactions.append(-other)
        
    def __str__(self):
        return f'{self.name} account - balance: {self.balance}'

if __name__ == "__main__":
    account = Account(name='kappa', start_balance=10)
    account - 5
    print(account)