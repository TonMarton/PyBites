scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
ranks = 'white yellow orange green blue brown black paneled red'.split()
BELTS = dict(zip(scores, ranks))


class NinjaBelt:

    def __init__(self, score=0):
        self._score = score
        self._last_earned_belt = self._get_belt(self._score)

    def _get_belt(self, new_score: int):
        """Might be a useful helper"""
        curr_belt = None
        for score, rank in BELTS.items():
            if score <= new_score:
                curr_belt = rank 
            else:
                break
        return curr_belt

    def _get_score(self):
        return self._score

    def _set_score(self, new_score: int):
        if not isinstance(new_score, int):
            raise ValueError('Score takes an int')
        elif new_score < self._score:
            raise ValueError(f'Cannot lower score')
        

        new_belt = self._get_belt(new_score)
        if new_belt != self._last_earned_belt and new_score  > self._score:
            self._last_earned_belt = new_belt
            print(f'Congrats, you earned {new_score} points obtaining the PyBites Ninja {self._last_earned_belt.title()} Belt')
        else:
            print(f'Set new score to {new_score}')
        
        self._score = new_score
        
    score = property(_get_score, _set_score)


    