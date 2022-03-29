from statistics import mean, median
from decimal import Decimal

class IntList(list):
    
    @property
    def mean(self):
        return mean(self)

    @property
    def median(self):
        return median(self)

    def append(self, __object) -> None:
        if isinstance(__object, list):
            if not self._check_if_int_list(__object):
                raise TypeError
        elif not isinstance(__object, (int, float, Decimal)):
                raise TypeError

        if isinstance(__object, Decimal):
            __object = int(__object)

        return super().append(__object)

    def __add__(self, __x: list) -> list:
        if not self._check_if_int_list(__x):
            raise TypeError
        return super().__add__(__x)

    def __iadd__(self: list, __x: list) -> list:
        if not self._check_if_int_list(__x):
            raise TypeError
        return super().__iadd__(__x)

    @staticmethod
    def _check_if_int_list(list: list) -> bool:
        
        return all(isinstance(e, int) for e in list)