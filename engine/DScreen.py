from utils import *
from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtGui import QPixmap, QPainter, QResizeEvent
from PySide6.QtCore import Qt, QEvent

class DScreen(QWidget):
    def __init__(self, parent: QWidget | None = None, image_path: str | None = None) -> None:
        super().__init__(parent)

        if isinstance(image_path, str):
            self.fullres_background_pixmap = QPixmap(image_path)

        self.scaled_background_pixmap = None
        self.box_layout = QVBoxLayout(self)
        self.box_layout.setContentsMargins(0, 0, 0, 0)
    
    def resizeEvent(self, event: QResizeEvent) -> None:
        super().resizeEvent(event)
        if not self.fullres_background_pixmap.isNull():
            self.scaled_background_pixmap = self.fullres_background_pixmap.scaled(
                self.size(), 
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )

    def paintEvent(self, event: QEvent) -> None:
        if self.scaled_background_pixmap and not self.scaled_background_pixmap.isNull():
            painter = QPainter(self)
            x_offset = (self.width() - self.scaled_background_pixmap.width()) // 2
            y_offset = (self.height() - self.scaled_background_pixmap.height()) // 2
            painter.drawPixmap(x_offset, y_offset, self.scaled_background_pixmap)
