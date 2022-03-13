from abc import ABC, abstractmethod, abstractproperty
from xmlrpc.client import boolean


class Challenge(ABC):
    def __init__(self, number: int, title: str):
        self.number = number
        self.title = title

    @abstractmethod
    def verify(self):
        pass

    @property
    @abstractmethod
    def pretty_title(self):
        pass

class BlogChallenge(Challenge):
    
    def __init__(self, number: int, title: str, merged_prs):
        super().__init__(number, title)
        self.merged_prs = merged_prs

    def verify(self, pr) -> bool:
        return pr in self.merged_prs
    
    @property
    def pretty_title(self):
        return f'PCC{self.number} - {self.title}'

class BiteChallenge(Challenge):

    def __init__(self, number: int, title: str, result: str):
        super().__init__(number, title)
        self.result = result
    
    def verify(self, result):
        return self.result is result

    @property
    def pretty_title(self):
        return f'Bite {self.number}. {self.title}'