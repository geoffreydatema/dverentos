from utils import *
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QLineEdit
from PySide6.QtGui import Qt

class DConsole(QWidget):
    def __init__(self, parent=None, game_manager=None):
        super().__init__(parent)
        self.game_manager = game_manager

        self.setGeometry(0, 0, self.parent().width(), self.parent().height())
        self.layout = QVBoxLayout(self)
        
        self.input_field = QLineEdit()
        self.input_field.setFixedHeight(24)
        self.input_field.setStyleSheet("background: rgba(128, 128, 128, 255); border: 0; font-size: 16px")
        
        self.layout.addStretch()
        self.layout.addWidget(self.input_field)

        self.input_field.returnPressed.connect(self.parse)

        self.setVisible(False)

    def parse(self):
        raw_command = self.input_field.text().split(" ")
        command_types = ("set", "get") #@! move to /data
        if raw_command[0] not in command_types:
            syntax_error("Command not recognized")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.setVisible(False)
            self.parent().setFocus()
