from utils import *
from PySide6.QtCore import Qt
from engine.DItemSlot import DItemSlot

class DToolSlot(DItemSlot):
    def __init__(self, r, c, parent=None):
        super().__init__(r, c, parent)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            print(f"tool slot at {self.row}, {self.col}")
        super().mousePressEvent(event)
