from enum import Enum, unique

@unique
class Player(Enum):
    Empty = 0,
    Red = 1,
    Blue = 2,
    Black = 3

    def __int__(self):
        return self.value
