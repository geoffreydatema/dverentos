from utils import *
from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtGui import QPixmap, QPainter
from PySide6.QtCore import Qt

class DScreen(QWidget):
    def __init__(self, image_path):
        super().__init__()
        self.fullres_background_pixmap = QPixmap(image_path)
        self.scaled_background_pixmap = None
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
    
    def resizeEvent(self, event):
        super().resizeEvent(event)
        if not self.fullres_background_pixmap.isNull():
            self.scaled_background_pixmap = self.fullres_background_pixmap.scaled(
                self.size(), 
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )

    def paintEvent(self, event):
        if self.scaled_background_pixmap and not self.scaled_background_pixmap.isNull():
            painter = QPainter(self)
            x_offset = (self.width() - self.scaled_background_pixmap.width()) // 2
            y_offset = (self.height() - self.scaled_background_pixmap.height()) // 2
            painter.drawPixmap(x_offset, y_offset, self.scaled_background_pixmap)
