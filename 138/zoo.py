class Animal:

    SEQUENCE_START = 10001
    _zoo: list = []

    def __init__(self, name: str):
        self._name: str = name.title()
        self._zoo.append(self._name)

    def __str__(self):
        index = self.SEQUENCE_START + self._zoo.index(self._name)
        return f'{index}. {self._name}'

    @classmethod
    def zoo(cls):
        return '\n'.join(f'{cls.SEQUENCE_START + index}. {name}' for index, name in enumerate(cls._zoo))