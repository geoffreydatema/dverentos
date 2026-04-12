from utils import *
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class DScreen(QWidget):
    def __init__(self, image_path):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.background = QLabel()
        self.background.setAlignment(Qt.AlignCenter)
        self.background.setMinimumSize(1, 1) 
        self.background.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)

        self.background_pixmap = QPixmap(image_path)
        
        self.layout.addWidget(self.background)
    
    def resizeEvent(self, event):
        super().resizeEvent(event)
        if not self.background_pixmap.isNull():
            scaled_pix = self.background_pixmap.scaled(
                self.size(), 
                Qt.KeepAspectRatio, 
                Qt.SmoothTransformation
            )
            self.background.setPixmap(scaled_pix)
