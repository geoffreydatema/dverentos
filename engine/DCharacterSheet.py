from utils import *
from PySide6.QtWidgets import QFrame, QVBoxLayout, QPushButton
from PySide6.QtGui import Qt

class DCharacterSheet(QFrame):
    def __init__(self, parent=None, engine_manager=None):
        super().__init__(parent)
        self.engine_manager = engine_manager

        self.setVisible(False)
        self.update_geometry()
        self.setStyleSheet("""
                           DCharacterSheet {
                                background: rgb(10, 20, 30);
                           }
                           """)
        self.layout = QVBoxLayout(self)

    def update_geometry(self):
        self.setGeometry(0, 0, self.parent().width(), self.parent().height())
