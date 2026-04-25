from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout
from PySide6.QtCore import Qt

class DCharacterValue(QWidget):
    def __init__(self, parent=None, name="PLACEHOLDER"):
        super().__init__(parent)

        self.layout = QHBoxLayout(self)

        self.name = QLabel(name)
        # self.label.setAlignment(Qt.AlignLeft)
        self.base = QLabel("0")
        self.minus = QLabel("0")
        self.plus = QLabel("0")
        self.total = QLabel("0")

        self.layout.addWidget(self.name)
        self.layout.addWidget(self.base)
        self.layout.addWidget(self.minus)
        self.layout.addWidget(self.plus)
        self.layout.addWidget(self.total)
