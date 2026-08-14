from utils import *
from PySide6.QtWidgets import QFrame, QSizePolicy
from PySide6.QtGui import QMouseEvent
from PySide6.QtCore import Qt

class DWeaponSlot(QFrame):
    def __init__(self, r, c, parent=None):
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

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            print(f"weapon slot at {self.row}, {self.col}")
        super().mousePressEvent(event)
