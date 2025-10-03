import copy
from Battleship import Battleship

class Player:
    def __init__(self, name: str, battleship: Battleship):
        self.name = name
        self.battleship = copy.deepcopy(battleship)