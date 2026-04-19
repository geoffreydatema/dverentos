from utils import *
from PySide6.QtWidgets import QWidget, QFrame, QStackedWidget, QHBoxLayout, QPushButton
from PySide6.QtGui import Qt
from engine.DCharacterUI import DCharacterUI
from engine.DVaultUI import DVaultUI
from engine.DCraftingUI import DCraftingUI
from engine.DArchiveUI import DArchiveUI
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

        self.character_ui = DCharacterUI(parent=self.account_ui_stack)
        self.vault_ui = DVaultUI(parent=self.account_ui_stack)
        self.crafting_ui = DCraftingUI(parent=self.account_ui_stack)
        self.archive_ui = DArchiveUI(parent=self.account_ui_stack)
        self.account_ui_stack.addWidget(self.character_ui)
        self.account_ui_stack.addWidget(self.vault_ui)
        self.account_ui_stack.addWidget(self.crafting_ui)
        self.account_ui_stack.addWidget(self.archive_ui)

        self.screen_map = {
            DScreenID.CHARACTER: self.character_ui,
            DScreenID.VAULT: self.vault_ui,
            DScreenID.CRAFTING: self.crafting_ui,
            DScreenID.ARCHIVE: self.archive_ui
        }

        self.switch(DScreenID.CHARACTER)

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
        
        self.map_button.clicked.connect(self.toggle)
        self.character_button.clicked.connect(lambda: self.switch(DScreenID.CHARACTER))
        self.vault_button.clicked.connect(lambda: self.switch(DScreenID.VAULT))
        self.crafting_button.clicked.connect(lambda: self.switch(DScreenID.CRAFTING))
        self.archive_button.clicked.connect(lambda: self.switch(DScreenID.ARCHIVE))

    def switch(self, screen_id):
        target_widget = self.screen_map.get(screen_id)
        if target_widget:
            self.account_ui_stack.setCurrentWidget(target_widget)
        else:
            error(f"Screen ID {screen_id} not recognized by Account Manager")

    def update_geometry(self):
        parent_size = self.parent().size()
        self.setGeometry(0, 0, parent_size.width(), parent_size.height())

        self.account_ui_stack.setGeometry(0, 0, self.width(), self.height())

        target_ratio = 16 / 9
        window_w = self.width()
        window_h = self.height()
        window_ratio = window_w / window_h

        if window_ratio > target_ratio:
            canvas_h = window_h
            canvas_w = int(canvas_h * target_ratio)
        else:
            canvas_w = window_w
            canvas_h = int(canvas_w / target_ratio)

        x_offset = (window_w - canvas_w) // 2
        y_offset = (window_h - canvas_h) // 2

        bar_height = 48
        self.navigation_bar.setGeometry(x_offset, y_offset, canvas_w, bar_height)
        
        self.navigation_bar.raise_()

    def toggle(self):
        if self.isVisible():
            self.setVisible(False)
            self.parent().setFocus()
        else:
            self.setVisible(True)
            self.update_geometry()
            self.switch(DScreenID.CHARACTER)
