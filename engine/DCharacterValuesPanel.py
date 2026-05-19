from utils import *
from PySide6.QtWidgets import QWidget, QLabel, QGridLayout
from PySide6.QtCore import Qt
from data.engine_constants import CharacterValues
from data.engine_constants import DType

class DCharacterValuesPanel(QWidget):
    def __init__(self, parent=None, game_manager=None):
        super().__init__(parent)
        self.game_manager = game_manager

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
        stats = self.game_manager.player.get_stats(DType.STR)
        skills = self.game_manager.player.get_skills(DType.STR)
        mastery = self.game_manager.player.get_mastery(DType.STR)
        row = 0
        
        # Add the 6 stats
        self.add_spacer(row)
        row += 1
        for i in range(len(CharacterValues.STATS)):
            self.add_complex_value(row, CharacterValues.STATS[i].upper(), stats[CharacterValues.STATS[i]][0], stats[CharacterValues.STATS[i]][1], stats[CharacterValues.STATS[i]][2], stats[CharacterValues.STATS[i]][3])
            row += 1
        
        # Add the 12 skills
        self.add_spacer(row)
        row += 1
        for i in range(len(CharacterValues.SKILLS)):
            self.add_complex_value(row, CharacterValues.SKILLS[i].upper(), skills[CharacterValues.SKILLS[i]][0], skills[CharacterValues.SKILLS[i]][1], skills[CharacterValues.SKILLS[i]][2], skills[CharacterValues.SKILLS[i]][3])
            row += 1

        # Add the 6 masteries
        self.add_spacer(row)
        row += 1
        for i in range(len(CharacterValues.MASTERY)):
            self.add_simple_value(row, CharacterValues.MASTERY[i].upper(), mastery[CharacterValues.MASTERY[i]])
            row += 1

    def add_simple_value(self, row_index, name, total):
        name_label = QLabel(name)
        name_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        
        total_label = self.build_label(total, "white")
        
        self.layout.addWidget(name_label, row_index, 0)
        self.layout.addWidget(total_label, row_index, 4)

    def add_complex_value(self, row_index, name, base, boost, penalty, total):
        name_label = QLabel(name)
        name_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        
        base_label = self.build_label(base)
        plus_label = self.build_label(f"+{boost}", "green")
        minus_label = self.build_label(penalty, "red")
        total_label = self.build_label(total, "white")

        # Add to the Master Grid
        self.layout.addWidget(name_label, row_index, 0)
        self.layout.addWidget(base_label, row_index, 1)
        self.layout.addWidget(plus_label, row_index, 2)
        self.layout.addWidget(minus_label, row_index, 3)
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

    def build_label(self, text, color=None):
        label = QLabel(text)
        label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        if color:
            label.setStyleSheet(f"color: {color};")
        return label
