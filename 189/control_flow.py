from itertools import count
from typing import List

IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names: List[str]):
    counter: int = 0
    for name in names:
        first_c: str = name[0]
        if name[0] == QUIT_CHAR:
            break
        elif first_c == IGNORE_CHAR or first_c.isdigit():
            continue
        has_digit = False
        for c in name[1:]:
            if c.isdigit():
                has_digit =True
                break
        if has_digit:
            continue
        counter += 1
        yield name
        if MAX_NAMES == counter:
            break