from utils import *
from core.Player import Player

class GameManager():
    def __init__(self):
        self.player = Player(game_manager=self)

        # self.player.update_values()
        # info(self.player.get_stats())
