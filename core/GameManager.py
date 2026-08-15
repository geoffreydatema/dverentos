from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine.Dverentos import Dverentos

from utils import *
from core.Player import Player

class GameManager():
    def __init__(self, engine: Dverentos) -> None:
        self.player = Player(game_manager=self)

        # self.player.update_values()
        # info(self.player.get_stats())
