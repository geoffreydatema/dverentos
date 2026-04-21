from utils import *
from PySide6.QtCore import Qt
from engine.DItemSlot import DItemSlot

class DStatus(DItemSlot):
    def __init__(self, r, c, parent=None):
        super().__init__(r, c, parent)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            print(f"status at {self.row}, {self.col}")
        super().mousePressEvent(event)
