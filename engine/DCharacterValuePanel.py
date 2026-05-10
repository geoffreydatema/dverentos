from PySide6.QtWidgets import QWidget, QLabel, QGridLayout
from PySide6.QtCore import Qt
from data.engine_constants import CharacterValues

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

    def build(self):
        row = 0
        self.add_spacer(row)
        row += 1

        for stat in CharacterValues.STATS:
            self.add_stat_row(row, stat.upper())
            row += 1

        self.add_spacer(row)
        row += 1

        for skill in CharacterValues.SKILLS:
            self.add_stat_row(row, skill.upper())
            row += 1

        self.add_spacer(row)
        row += 1

        for mastery in CharacterValues.MASTERY:
            self.add_stat_row(row, mastery.upper())
            row += 1

    def add_stat_row(self, row_index, name):
        name_label = QLabel(name)
        name_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        
        base_label = self.create_val_label("9999")
        minus_label = self.create_val_label("-9999", "red")
        plus_label = self.create_val_label("+9999", "green")
        total_label = self.create_val_label("9999", "white")

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
        if color:
            label.setStyleSheet(f"color: {color};")
        return label
