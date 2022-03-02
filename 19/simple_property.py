from datetime import datetime
from webbrowser import get

NOW = datetime.now()


class Promo:

    def __init__(self, name: str, expires: datetime):
        self._expires = expires

    @property
    def expired(self):
        return NOW >= self._expires