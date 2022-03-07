class RecordScore():
    """Class to track a game's maximum score"""

    _score: int = None

    def __call__(self, score: int):
        if not self._score or score > self._score:
            self._score = score
        return self._score