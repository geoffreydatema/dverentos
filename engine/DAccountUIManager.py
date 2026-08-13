from utils import *
from PySide6.QtWidgets import QWidget, QFrame, QStackedWidget, QHBoxLayout, QPushButton
from PySide6.QtGui import Qt
from engine.DCharacterUI import DCharacterUI
from engine.DVaultUI import DVaultUI
from engine.DCraftingUI import DCraftingUI
from engine.DArchiveUI import DArchiveUI
from engine.DFont import DFont
from engine.DScreen import DScreen
from data.engine_constants import DScreenID

class DAccountUIManager(QFrame):
    def __init__(self, parent: QWidget, game_manager):
        super().__init__(parent)

        self.parent_widget = parent
        self.game_manager = game_manager
        
        self.setStyleSheet("""
            DAccountUIManager {
                background: rgb(10, 10, 10);
            }
            QPushButton:hover {
                background: rgb(80, 80, 80);
            }
            QPushButton:pressed {
                background: rgb(50, 50, 50);
            }
        """)

        self.setVisible(False)
        
        self.account_ui_stack = QStackedWidget(self)
        
        self.build_navigation() 

        self.character_ui = DCharacterUI(parent=self.account_ui_stack, game_manager=self.game_manager)
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

    def build_navigation_button(self, text):
        button = QPushButton(text)
        button.setFont(DFont.SANS_BOLD)
        return button

    def build_navigation(self):
        self.navigation_bar = QWidget(self)
        self.navigation_layout = QHBoxLayout(self.navigation_bar)
        self.navigation_layout.setContentsMargins(0, 0, 10, 0)
        self.navigation_layout.setSpacing(10)
        
        self.map_button = self.build_navigation_button("MAP")
        self.character_button = self.build_navigation_button("CHARACTER")
        self.vault_button = self.build_navigation_button("VAULT")
        self.crafting_button = self.build_navigation_button("CRAFTING")
        self.archive_button = self.build_navigation_button("ARCHIVE")

        self.navigation_layout.addStretch()

        for btn in [self.map_button, self.character_button, self.vault_button, 
                    self.crafting_button, self.archive_button]:
            btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
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
        parent_size = self.parent_widget.size()
        self.setGeometry(0, 0, parent_size.width(), parent_size.height())
        self.account_ui_stack.setGeometry(0, 0, self.width(), self.height())

        target_ratio = 16 / 9
        w, h = self.width(), self.height()
        
        if (w / h) > target_ratio:
            canvas_h = h
            canvas_w = int(h * target_ratio)
        else:
            canvas_w = w
            canvas_h = int(w / target_ratio)

        x_offset = (w - canvas_w) // 2
        y_offset = (h - canvas_h) // 2

        dynamic_bar_height = canvas_h // 18 
        
        self.navigation_bar.setGeometry(x_offset, y_offset, canvas_w, dynamic_bar_height)
                
        self.navigation_bar.raise_()

        active_screen = self.account_ui_stack.currentWidget()
        if isinstance(active_screen, DScreen):
            active_screen.update_geometry()

    def toggle(self):
        if self.isVisible():
            self.setVisible(False)
            self.parent_widget.setFocus()
        else:
            self.setVisible(True)
            self.update_geometry()
            self.switch(DScreenID.CHARACTER)
