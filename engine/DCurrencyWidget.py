from utils import *
from PySide6.QtWidgets import QFrame, QSizePolicy, QHBoxLayout, QLabel
from PySide6.QtCore import Qt

class DCurrencyWidget(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("""
                            QFrame {
                                background: rgb(80, 80, 80);
                                border: 1px solid rgb(30, 30, 30);
                            }
                            QLabel {
                                border: 0;
                                font-size: 14px;
                            }
                           """)
        self.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.amount_label = QLabel("9999")
        self.amount_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.symbol_label = QLabel("X")
        self.symbol_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.layout.addWidget(self.symbol_label, 1)
        self.layout.addWidget(self.amount_label, 5)
