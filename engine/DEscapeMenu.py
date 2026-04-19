from utils import *
from PySide6.QtWidgets import QFrame, QVBoxLayout, QPushButton
from PySide6.QtGui import Qt

class DEscapeMenu(QFrame):
    def __init__(self, parent=None, engine_manager=None):
        super().__init__(parent)
        self.engine_manager = engine_manager

        self.setVisible(False)
        self.update_geometry()
        self.setStyleSheet("""
                           DEscapeMenu {
                                background: rgb(30, 30, 30);
                           }

                           QPushButton {
                                background: rgb(60, 60, 60);
                           }

                           QPushButton:hover {
                                background: rgb(80, 80, 80);
                           }

                           QPushButton:pressed {
                                background: rgb(50, 50, 50);
                           }
                           """)
        self.layout = QVBoxLayout(self)

        self.exit_button = QPushButton("Exit")
        self.exit_button.setFixedWidth(100)

        self.layout.addWidget(self.exit_button, alignment=Qt.AlignCenter)

        self.exit_button.clicked.connect(self.handle_exit)

    def update_geometry(self):
        self.setGeometry(0, 0, self.parent().width(), self.parent().height())

    def handle_exit(self):
        self.engine_manager.quit()

    def toggle(self):
        if self.isVisible():
            self.setVisible(False)
            self.parent().setFocus()
        else:
            self.setVisible(True)
