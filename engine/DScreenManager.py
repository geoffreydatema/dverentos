from PySide6.QtWidgets import QStackedWidget, QWidget, QVBoxLayout, QLabel

class DScreenManager(QStackedWidget):
    def __init__(self, game_manager):
        super().__init__()
        self.game_manager = game_manager

        self.screen = self.create_screen()

        self.addWidget(self.screen)
    
    def create_screen(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)
        # label = QLabel("hello world")
        # layout.addWidget(label)
        return widget
