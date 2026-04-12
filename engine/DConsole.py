from utils import *
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QLineEdit
from PySide6.QtGui import Qt
from PySide6.QtCore import QCoreApplication

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
        if not raw_command:
            error("No command entered")
        
        operation = raw_command[0].lower()
        args = raw_command[1:]

        if operation == "hi":
            info("Hello right back at ya")
        elif operation == "close":
            self.setVisible(False)
            self.parent().setFocus()
        elif operation == "quit" or operation == "exit":
            info("Force quit")
            QCoreApplication.quit()
        else:
            warning("Command not recognized")
        
        self.input_field.setText("")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.setVisible(False)
            self.parent().setFocus()
