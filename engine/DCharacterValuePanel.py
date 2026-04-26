from PySide6.QtWidgets import QWidget, QLabel, QGridLayout
from PySide6.QtCore import Qt

class DCharacterValuePanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setStyleSheet("""
                            QWidget {
                                background: rgb(60, 60, 60);
                            }
                            """)
        self.layout = QGridLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(4)
        
        self.layout.setColumnStretch(0, 4) 
        for i in range(1, 5):
            self.layout.setColumnStretch(i, 2)

        self.stats = {}

    def add_stat_row(self, row_index, name):
        name_label = QLabel(name)
        name_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        
        base_label = self.create_val_label("999")
        minus_label = self.create_val_label("-999", "red")
        plus_label = self.create_val_label("+999", "green")
        total_label = self.create_val_label("999", "white")

        # Add to the Master Grid
        self.layout.addWidget(name_label, row_index, 0)
        self.layout.addWidget(base_label, row_index, 1)
        self.layout.addWidget(minus_label, row_index, 2)
        self.layout.addWidget(plus_label, row_index, 3)
        self.layout.addWidget(total_label, row_index, 4)

        # Store references by name for easy updating
        self.stats[name] = {
            "base": base_label, "minus": minus_label, 
            "plus": plus_label, "total": total_label
        }

    def add_spacer(self, row_index, height=16):
        spacer = QWidget()
        spacer.setMinimumHeight(height)
        self.layout.addWidget(spacer, row_index, 0, 1, 5)

    def create_val_label(self, text, color=None):
        label = QLabel(text)
        label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        # Force a minimum width based on '888' to reserve space for 3 digits
        # metrics = label.fontMetrics()
        # label.setMinimumWidth(metrics.horizontalAdvance("888") + 10)
        if color:
            label.setStyleSheet(f"color: {color};")
        return label
