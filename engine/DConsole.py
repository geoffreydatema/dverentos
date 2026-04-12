from PySide6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QLineEdit
from PySide6.QtGui import Qt

class DConsole(QWidget):
    def __init__(self, parent=None, game_manager=None):
        super().__init__(parent)
        self.parent = parent
        self.game_manager = game_manager

        self.setGeometry(0, 0, self.parent.width(), self.parent.height())
        self.layout = QVBoxLayout(self)
        
        self.input_field = QLineEdit()
        self.input_field.setStyleSheet("background: rgba(128, 128, 128, 255); border: 0")
        
        self.layout.addWidget(self.input_field)

        self.setVisible(False)
