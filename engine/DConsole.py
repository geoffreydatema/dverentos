from utils import *
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit
from PySide6.QtGui import Qt, QGuiApplication
from PySide6.QtCore import QCoreApplication

class DConsole(QWidget):
    def __init__(self, parent=None, game_manager=None):
        super().__init__(parent)
        self.game_manager = game_manager

        self.update_geometry()
        self.layout = QVBoxLayout(self)
        
        self.input_field = QLineEdit()
        self.input_field.setFixedHeight(24)
        self.input_field.setStyleSheet("""
                                       background: rgb(0, 0, 0);
                                       font-size: 16px;
                                       border: 1px solid rgb(255, 255, 255);
                                       """)
        
        self.layout.addStretch()
        self.layout.addWidget(self.input_field)

        self.input_field.returnPressed.connect(self.parse)

        self.setVisible(False)

    def update_geometry(self):
        self.setGeometry(0, 0, self.parent().width(), self.parent().height())

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
        elif operation == "set":
            self.handle_set(args)
        else:
            warning("Command not recognized")
        
        self.input_field.setText("")

    def handle_set(self, args):
        variable = args[0].lower()
        values = args[1:]

        if variable == "resolution":
            if len(values) != 2:
                error("Incorrect number of args passed for resolution change")
                return
            try:
                width = int(values[0])
                height = int(values[1])
            except ValueError:
                error("Resolution args must be int")
                return
            
            self.parent().update_geometry(w=width, h=height)
            info(f"Resolution set to {width} x {height}")

        if variable == "fullscreen":
            if len(values) != 1:
                error("Incorrect number of args passed for fullscreen setting")
                return
            if values[0] == "true":
                self.parent().update_geometry(fullscreen=True)
                info("Application set to fullscreen")
            elif values[0] == "false":
                self.parent().update_geometry(fullscreen_windowed=True)
                info("Application set to fullscreen windowed")
            else:
                error('Fullscreen arg must be "true" or "false"')
                return
            
        if variable == "fullscreen_windowed":
            if len(values) != 1:
                error("Incorrect number of args passed for fullscreen setting")
                return
            if values[0] == "true":
                self.parent().update_geometry(fullscreen_windowed=True)
                info("Application set to fullscreen windowed")
            elif values[0] == "false":
                self.parent().update_geometry(fullscreen=True)
                info("Application set to fullscreen")
            else:
                error('Fullscreen arg must be "true" or "false"')
                return

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.setVisible(False)
            self.parent().setFocus()
