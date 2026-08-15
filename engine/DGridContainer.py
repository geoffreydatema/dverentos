from utils import *
from PySide6.QtWidgets import QWidget, QFrame, QSizePolicy

class DGridContainer(QFrame):
    def __init__(self, parent: QWidget, r: int, c: int) -> None:
        super().__init__(parent)
        self.setStyleSheet("""
                            QFrame {
                                background: rgb(40, 40, 40);
                            }
                           """)

        self.row = r
        self.col = c
        
        self.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
