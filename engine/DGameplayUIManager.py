from utils import *
from PySide6.QtWidgets import QStackedWidget
from engine.DScreen import DScreen
from data.engine_constants import DScreenID

class DGameplayUIManager(QStackedWidget):
    def __init__(self, parent, game_manager):
        super().__init__(parent)
        self.game_manager = game_manager
        self.screen_map = {}

        self.main_menu = self.add_screen("assets/placeholder/fullscreen_placeholder_v001.jpg")
        self.placeholder = self.add_screen("assets/placeholder/fullscreen_placeholder_A_v001.jpg")

        self.screen_map[DScreenID.MAIN_MENU] = self.main_menu
        self.screen_map[DScreenID.PLACEHOLDER] = self.placeholder

        self.switch(DScreenID.MAIN_MENU)
    
    def add_screen(self, asset_path):
        screen = DScreen(asset_path)
        self.addWidget(screen)
        return screen

    def switch(self, screen_id):
        target_widget = self.screen_map.get(screen_id)
        if target_widget:
            self.setCurrentWidget(target_widget)
        else:
            error(f"Screen ID {screen_id} not recognized by Screen Manager")
