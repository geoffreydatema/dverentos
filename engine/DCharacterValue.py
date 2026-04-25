from PySide6.QtWidgets import QWidget, QLabel, QGridLayout
from PySide6.QtCore import Qt

class DCharacterValue(QWidget):
    def __init__(self, parent=None, name="PLACEHOLDER"):
        super().__init__(parent)

        self.setStyleSheet("""
                            QWidget {
                                background: rgb(255, 0, 0); /*placeholder colour for visibility*/
                            }
                           """)

        self.layout = QGridLayout(self)
        self.layout.setContentsMargins(0, 2, 0, 2)
        self.layout.setSpacing(4)
        self.layout.setColumnStretch(0, 0) 
        for i in range(1, 5):
            self.layout.setColumnStretch(i, 2)

        self.name = QLabel(name)
        self.name.setAlignment(Qt.AlignRight)
        self.base = QLabel("0")
        self.minus = QLabel("0")
        self.plus = QLabel("0")
        self.total = QLabel("0")

        self.layout.addWidget(self.name, 0, 0)
        self.layout.addWidget(self.base, 0, 1)
        self.layout.addWidget(self.minus, 0, 2)
        self.layout.addWidget(self.plus, 0, 3)
        self.layout.addWidget(self.total, 0, 4)
