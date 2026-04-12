from utils import *
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit
from PySide6.QtGui import Qt

class DConsole(QWidget):
    def __init__(self, parent=None, engine_manager=None):
        super().__init__(parent)
        self.engine_manager = engine_manager

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
            self.engine_manager.quit()
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
            self.engine_manager.set_resolution(values[0], values[1])

        if variable == "fullscreen":
            if len(values) != 1:
                error("Incorrect number of args passed for fullscreen setting")
                return
            self.engine_manager.set_fullscreen(values[0])
            
        if variable == "fullscreen_windowed":
            if len(values) != 1:
                error("Incorrect number of args passed for fullscreen setting")
                return
            self.engine_manager.set_fullscreen_windowed(values[0])

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.setVisible(False)
            self.parent().setFocus()
