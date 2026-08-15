from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QFrame, QSizePolicy

from utils import *

class DItemSlot(QFrame):
    def __init__(self, parent: QWidget, r: int, c: int) -> None:
        super().__init__(parent)
        self.setStyleSheet("""
                            QFrame {
                                background: rgb(50, 50, 50);
                                border: 1px solid rgb(30, 30, 30);
                            }
                            QFrame:hover {
                                background: rgb(60, 60, 60);
                                border: 1px solid rgb(30, 30, 30);
                            }
                           """)

        self.row = r
        self.col = c
        self.item = None
        
        self.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
