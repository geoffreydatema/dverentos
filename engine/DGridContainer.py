from utils import *
from PySide6.QtWidgets import QFrame, QSizePolicy

class DGridContainer(QFrame):
    def __init__(self, r, c, parent=None):
        super().__init__(parent)
        self.setStyleSheet("""
                            QFrame {
                                background: rgb(40, 40, 40);
                            }
                           """)

        self.row = r
        self.col = c
        
        self.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
