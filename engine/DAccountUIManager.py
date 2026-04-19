from utils import *
from PySide6.QtWidgets import QWidget, QFrame, QStackedWidget, QVBoxLayout, QHBoxLayout, QPushButton
from PySide6.QtGui import Qt
from engine.DScreen import DScreen
from engine.DCharacterSheet import DCharacterSheet
from data.engine_constants import DScreenID

class DAccountUIManager(QFrame):
    def __init__(self, parent, game_manager):
        super().__init__(parent)
        self.setVisible(False)
        self.game_manager = game_manager

        self.setStyleSheet("""
            DAccountUIManager {
                background: rgb(10, 10, 10);
            }
            QPushButton {
                background: rgb(60, 60, 60);
                color: white;
                border: 1px solid rgb(80, 80, 80);
                padding: 5px 15px;
            }
            QPushButton:hover {
                background: rgb(80, 80, 80);
            }
            QPushButton:pressed {
                background: rgb(50, 50, 50);
            }
        """)
        
        self.account_ui_stack = QStackedWidget(self)
        
        self.build_navigation() 

        self.character_screen = DCharacterSheet(parent=self.account_ui_stack)
        self.account_ui_stack.addWidget(self.character_screen)

        self.screen_map = {
            DScreenID.CHARACTER: self.character_screen
        }

    def build_navigation(self):
        self.navigation_bar = QWidget(self)
        self.navigation_layout = QHBoxLayout(self.navigation_bar)
        self.navigation_layout.setContentsMargins(10, 10, 10, 4)
        self.navigation_layout.setSpacing(10)
        
        self.map_button = QPushButton("MAP")
        self.character_button = QPushButton("CHARACTER")
        self.vault_button = QPushButton("VAULT")
        self.crafting_button = QPushButton("CRAFTING")
        self.archive_button = QPushButton("ARCHIVE")

        self.navigation_layout.addStretch()

        for btn in [self.map_button, self.character_button, self.vault_button, 
                    self.crafting_button, self.archive_button]:
            btn.setFocusPolicy(Qt.NoFocus)
            self.navigation_layout.addWidget(btn)
        
        self.character_button.clicked.connect(lambda: self.switch(DScreenID.CHARACTER))

    def switch(self, screen_id):
        target_widget = self.screen_map.get(screen_id)
        if target_widget:
            self.account_ui_stack.setCurrentWidget(target_widget)
        else:
            error(f"Screen ID {screen_id} not recognized by Account Manager")

    def update_geometry(self):
        """ Manually layer the widgets since we aren't using a vertical layout """
        parent_size = self.parent().size()
        self.setGeometry(0, 0, parent_size.width(), parent_size.height())

        # Make the stack fill the FULL area (for full-res art)
        self.account_ui_stack.setGeometry(0, 0, self.width(), self.height())

        # Float the navigation bar at the top
        bar_height = 48
        self.navigation_bar.setGeometry(0, 0, self.width(), bar_height)
        
        # Ensure the nav bar stays visually on top of the stack
        self.navigation_bar.raise_()

    def toggle(self):
        if self.isVisible():
            self.setVisible(False)
            self.parent().setFocus()
        else:
            self.setVisible(True)
            self.update_geometry()
