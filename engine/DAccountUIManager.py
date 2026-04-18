from utils import *
from PySide6.QtWidgets import QStackedWidget
from engine.DScreen import DScreen
from data.engine_constants import DScreenID

class DAccountUIManager(QStackedWidget):
    def __init__(self, parent, game_manager):
        super().__init__(parent)

        self.setVisible(False)
        self.game_manager = game_manager
        self.screen_map = {}

        self.main_menu = self.add_screen("assets/placeholder/fullscreen_placeholder_v001.jpg")
        self.placeholder = self.add_screen("assets/placeholder/fullscreen_placeholder_A_v001.jpg")

        self.screen_map[DScreenID.PLACEHOLDER] = self.placeholder

        self.switch(DScreenID.PLACEHOLDER)
    
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

    def update_geometry(self):
        self.setGeometry(0, 0, self.parent().width(), self.parent().height())

    #@! add keyboard event to turn off account ui
