from utils import *
from PySide6.QtWidgets import QFrame, QSizePolicy, QHBoxLayout, QLabel
from PySide6.QtCore import Qt
from engine.DFont import DFont

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
        self.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        self.box_layout = QHBoxLayout(self)
        self.box_layout.setContentsMargins(0, 0, 0, 0)
        self.box_layout.setSpacing(0)
        self.amount_label = QLabel("9999")
        self.amount_label.setFont(DFont.SANS_REGULAR)
        self.amount_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        self.symbol_label = QLabel("X")
        self.symbol_label.setFont(DFont.SERIF_REGULAR)
        self.symbol_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.box_layout.addWidget(self.symbol_label, 1)
        self.box_layout.addWidget(self.amount_label, 5)
