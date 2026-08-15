from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QMouseEvent
from PySide6.QtCore import Qt

from utils import *
from engine.DItemSlot import DItemSlot

class DInventorySlot(DItemSlot):
    def __init__(self, parent: QWidget, r: int, c: int) -> None:
        super().__init__(parent, r, c)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            print(f"inventory slot at {self.row}, {self.col}")
        super().mousePressEvent(event)
