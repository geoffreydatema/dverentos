from utils import *
from PySide6.QtWidgets import QWidget, QFrame, QStackedWidget, QVBoxLayout, QHBoxLayout, QPushButton
from PySide6.QtGui import Qt
from engine.DScreen import DScreen
from engine.DCharacterSheet import DCharacterSheet
from data.engine_constants import DScreenID

class DAccountUIManager(QFrame):
    def __init__(self, parent, game_manager):
        super().__init__(parent)

        self.setStyleSheet("""
                           DAccountUIManager {
                                background: rgb(10, 10, 10);
                           }

                           QPushButton {
                                background: rgb(60, 60, 60);
                           }

                           QPushButton:hover {
                                background: rgb(80, 80, 80);
                           }

                           QPushButton:pressed {
                                background: rgb(50, 50, 50);
                           }
                           """)
        
        self.setVisible(False)
        self.game_manager = game_manager

        self.character_screen = DCharacterSheet(self)
        
        self.screen_map = {}
        self.screen_map[DScreenID.CHARACTER] = self.character_screen

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.build_navigation()
        self.account_ui_stack = QStackedWidget()
        self.layout.addWidget(self.account_ui_stack)
        self.account_ui_stack.addWidget(self.character_screen)

    def build_navigation(self):
        self.navigation_bar = QWidget()
        self.navigation_layout = QHBoxLayout(self.navigation_bar)
        self.navigation_layout.setContentsMargins(10, 10, 10, 4)
        
        self.map_button = QPushButton("MAP")
        self.character_button = QPushButton("CHARACTER")
        self.vault_button = QPushButton("VAULT")
        self.crafting_button = QPushButton("CRAFTING")
        self.archive_button = QPushButton("ARCHIVE")

        self.map_button.setFocusPolicy(Qt.NoFocus)
        self.character_button.setFocusPolicy(Qt.NoFocus)
        self.vault_button.setFocusPolicy(Qt.NoFocus)
        self.crafting_button.setFocusPolicy(Qt.NoFocus)
        self.archive_button.setFocusPolicy(Qt.NoFocus)
        
        self.navigation_layout.addStretch()
        self.navigation_layout.addWidget(self.map_button)
        self.navigation_layout.addWidget(self.character_button)
        self.navigation_layout.addWidget(self.vault_button)
        self.navigation_layout.addWidget(self.crafting_button)
        self.navigation_layout.addWidget(self.archive_button)

        self.character_button.clicked.connect(lambda: self.switch(DScreenID.CHARACTER))

        self.layout.addWidget(self.navigation_bar)

    def add_screen(self, asset_path):
        screen = DScreen(asset_path)
        self.account_ui_stack.addWidget(screen)
        return screen

    def switch(self, screen_id):
        target_widget = self.screen_map.get(screen_id)
        if target_widget:
            self.account_ui_stack.setCurrentWidget(target_widget)
        else:
            error(f"Screen ID {screen_id} not recognized by Screen Manager")

    def update_geometry(self):
        self.setGeometry(0, 0, self.parent().width(), self.parent().height())

    def toggle(self):
        if self.isVisible():
            self.setVisible(False)
            self.parent().setFocus()
        else:
            self.setVisible(True)
