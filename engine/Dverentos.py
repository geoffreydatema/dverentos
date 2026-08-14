from utils import *
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QGuiApplication, Qt, QKeyEvent, QResizeEvent
from PySide6.QtCore import QObject, QEvent
from engine.DEngineManager import DEngineManager
from engine.DGameplayUIManager import DGameplayUIManager
from engine.DAccountUIManager import DAccountUIManager
from engine.DEscapeMenu import DEscapeMenu
from engine.DConsole import DConsole
from core.GameManager import GameManager

class Dverentos(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("DVERENTOS")
        self.setStyleSheet("""
                           Dverentos {
                                background: rgb(0, 0, 0);
                           }
                           """)

        self.engine_manager = DEngineManager(engine=self)
        self.game_manager = GameManager(engine=self)
        self.gameplay_ui_manager = DGameplayUIManager(parent=self, game_manager=self.game_manager)
        self.account_ui_manager = DAccountUIManager(parent=self, game_manager=self.game_manager)
        self.setCentralWidget(self.gameplay_ui_manager)

        self.escape_menu = DEscapeMenu(parent=self, engine_manager=self.engine_manager)
        self.console = DConsole(parent=self, engine_manager=self.engine_manager)

        self.engine_manager.apply_settings()

        self.installEventFilter(self)

        # default screen
        self.account_ui_manager.toggle()

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if isinstance(event, QKeyEvent) and event.type() == QEvent.Type.KeyPress:
            key = event.key()

            if key == Qt.Key.Key_Escape:
                self.escape_menu.toggle()

            elif key == Qt.Key.Key_QuoteLeft:
                self.console.toggle()

            elif key == Qt.Key.Key_Tab:
                self.account_ui_manager.toggle()
        
        return super().eventFilter(watched, event)
    
    def center_window(self) -> None:
        screen = QGuiApplication.primaryScreen().availableGeometry()
        size = self.frameGeometry()
        center_point = screen.center()
        size.moveCenter(center_point)
        self.move(size.topLeft())

    def resizeEvent(self, event: QResizeEvent) -> None:
        super().resizeEvent(event)
        self.account_ui_manager.update_geometry()
        self.escape_menu.update_geometry()
        self.console.update_geometry()

    def update_geometry(self, w: int=1280, h: int=720, fullscreen: bool=False, fullscreen_windowed: bool=False) -> None:
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

    def changeEvent(self, event: QEvent) -> None:
        if event.type() == QEvent.Type.WindowStateChange:
            if self.isMaximized() or self.windowState() == Qt.WindowState.WindowNoState:
                self.account_ui_manager.update_geometry()
        
        super().changeEvent(event)
