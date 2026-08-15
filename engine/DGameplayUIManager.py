from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.GameManager import GameManager

from PySide6.QtWidgets import QWidget, QStackedWidget

from utils import *
from engine.DScreen import DScreen
from data.engine_constants import DScreenID

class DGameplayUIManager(QStackedWidget):
    def __init__(self, parent: QWidget, game_manager: GameManager):
        super().__init__(parent)
        self.game_manager = game_manager
        
        self.main_menu = DScreen(parent=self, image_path="assets/placeholder/main_menu_placeholder_v001.jpg")
        self.addWidget(self.main_menu)
        self.map_placeholder = DScreen(parent=self, image_path="assets/placeholder/map_placeholder_v001.jpg")
        self.addWidget(self.map_placeholder)

        self.screen_map = {
            DScreenID.MAIN_MENU: self.main_menu,
            DScreenID.PLACEHOLDER: self.map_placeholder
        }

        self.switch(DScreenID.MAIN_MENU)

    def switch(self, screen_id: DScreenID):
        target_widget = self.screen_map.get(screen_id)
        if target_widget:
            self.setCurrentWidget(target_widget)
        else:
            error(f"Screen ID {screen_id} not recognized by Screen Manager")
