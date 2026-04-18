from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QGuiApplication, Qt
from engine.DEngineManager import DEngineManager
from engine.DGameplayUIManager import DGameplayUIManager
from engine.DAccountUIManager import DAccountUIManager
# from engine.DCharacterSheet import DCharacterSheet
from engine.DEscapeMenu import DEscapeMenu
from engine.DConsole import DConsole
from core import DGameManager
from utils import *

class Dverentos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DVERENTOS")
        self.setStyleSheet("""
                           background: rgb(0, 0, 0);
                           """)

        self.engine_manager = DEngineManager(engine=self)
        self.game_manager = DGameManager()
        self.gameplay_ui_manager = DGameplayUIManager(parent=self, game_manager=self.game_manager)
        self.account_ui_manager = DAccountUIManager(parent=self, game_manager=self.game_manager)
        self.setCentralWidget(self.gameplay_ui_manager)

        self.escape_menu = DEscapeMenu(parent=self, engine_manager=self.engine_manager)
        self.console = DConsole(parent=self, engine_manager=self.engine_manager)

        self.engine_manager.apply_settings()

    def center_window(self):
        screen = QGuiApplication.primaryScreen().availableGeometry()
        size = self.frameGeometry()
        center_point = screen.center()
        size.moveCenter(center_point)
        self.move(size.topLeft())

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.escape_menu.setVisible(not self.escape_menu.isVisible())

        elif event.key() == Qt.Key_Tab:
            self.account_ui_manager.setVisible(True)

        elif event.key() == Qt.Key_QuoteLeft:
            self.console.setVisible(not self.console.isVisible())
            if self.console.isVisible():
                self.console.input_field.setFocus()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.account_ui_manager.update_geometry()
        self.escape_menu.update_geometry()
        self.console.update_geometry()

    def update_geometry(self, w=1280, h=720, fullscreen=False, fullscreen_windowed=False):
        final_width = w
        final_height = h

        if fullscreen:
            self.showFullScreen()
            return
        
        if fullscreen_windowed:
            self.showMaximized()
            return
        
        self.showNormal()
        self.setGeometry(0, 0, final_width, final_height)
        self.center_window()
