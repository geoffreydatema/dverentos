from PySide6.QtWidgets import QWidget, QFrame, QGridLayout, QSizePolicy
from PySide6.QtCore import Qt

class DInventoryPreviewPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setStyleSheet("""
                            QFrame {
                                background: rgb(60, 60, 60);
                                border: 1px solid rgb(30, 30, 30);
                            }
                            """)
        self.layout = QGridLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        
        for i in range(0, 16):
            self.layout.setColumnStretch(i, 1)  

    def build(self):

        for r in range(0, 4): 
            for c in range(0, 16):
                cell = QFrame()
                self.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
                self.layout.addWidget(cell, r, c)

