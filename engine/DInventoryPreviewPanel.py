from PySide6.QtWidgets import QWidget, QFrame, QGridLayout, QSizePolicy

class DInventoryPreviewPanel(QWidget):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        
        self.setStyleSheet("""
                            QFrame {
                                background: rgb(60, 60, 60);
                                border: 1px solid rgb(30, 30, 30);
                            }
                            """)
        self.grid_layout = QGridLayout(self)
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.grid_layout.setSpacing(0)
        
        for i in range(0, 16):
            self.grid_layout.setColumnStretch(i, 1)  

    def build(self):

        for r in range(0, 4): 
            for c in range(0, 16):
                cell = QFrame()
                self.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
                self.grid_layout.addWidget(cell, r, c)

