from utils import *
from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QFrame, QSizePolicy, QVBoxLayout
from PySide6.QtCore import Qt
from engine.DScreen import DScreen
from data.engine_constants import DFontSize

class DCharacterUI(DScreen):
    def __init__(self, parent=None, engine_manager=None, image_path="assets/character_ui/character_ui_grid_v001.png"):
        super().__init__(parent, image_path)

        self.grid_container = QWidget(self)
        self.grid_layout = QGridLayout(self.grid_container)

        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.grid_layout.setSpacing(0)

        for i in range(32):
            self.grid_layout.setColumnStretch(i, 1)
        for i in range(18):
            self.grid_layout.setRowStretch(i, 1)

        self.grid_container.setParent(self)
        self.build_ui()

    def build_ui(self):
        self.label_wrapper = QFrame()
        self.label_wrapper.setStyleSheet("background: rgb(30, 30, 30); border: none;")
        self.label_wrapper.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        
        wrapper_layout = QVBoxLayout(self.label_wrapper)
        wrapper_layout.setContentsMargins(0, 0, 0, 0)
        wrapper_layout.setSpacing(0)

        self.label = QLabel("STAT PLACEHOLDER")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("color: white; background: transparent;")
        
        wrapper_layout.addWidget(self.label)
        self.grid_layout.addWidget(self.label_wrapper, 5, 2, 1, 3)

        self.slot = QFrame()
        self.slot.setStyleSheet("background: rgb(20, 20, 128);")
        self.slot.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.grid_layout.addWidget(self.slot, 2, 20, 1, 1)

    def resizeEvent(self, event):
        super().resizeEvent(event)

        self.update_geometry()
        
    def update_geometry(self):
        if not self.fullres_background_pixmap.isNull():
            self.scaled_background_pixmap = self.fullres_background_pixmap.scaled(
                self.size(), 
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )

        if self.scaled_background_pixmap:
            bg_w = self.scaled_background_pixmap.width()
            bg_h = self.scaled_background_pixmap.height()
            
            x_offset = (self.width() - bg_w) // 2
            y_offset = (self.height() - bg_h) // 2

            self.grid_container.setGeometry(x_offset, y_offset, bg_w, bg_h)
            
            if bg_h > 0:
                self.update_fonts()

    def update_fonts(self):
        h = self.grid_container.height()
        if h <= 0: return

        cell_height = h / 18
        new_size = int(cell_height * DFontSize.CHARACTER_UI_STATS)
        
        new_size = max(1, new_size) 
        
        font = self.label.font()
        font.setPixelSize(new_size)
        self.label.setFont(font)
