from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QGuiApplication
from engine.DScreenManager import DScreenManager
from core import DGameManager

class Dverentos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DVERENTOS")
        self.setGeometry(0, 0, 1280, 720)
        self.center_window()

        self.game_manager = DGameManager()

        self.screen_manager = DScreenManager(self.game_manager)

        self.setCentralWidget(self.screen_manager)

    def center_window(self):
        screen = QGuiApplication.primaryScreen().availableGeometry()
        size = self.frameGeometry()
        center_point = screen.center()
        size.moveCenter(center_point)
        self.move(size.topLeft())
