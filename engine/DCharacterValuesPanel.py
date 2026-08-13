from utils import *
from PySide6.QtWidgets import QWidget, QLabel, QGridLayout
from PySide6.QtCore import Qt
from data.engine_constants import CharacterValues
from data.engine_constants import DType
from engine.DFont import DFont

class DCharacterValuesPanel(QWidget):
    def __init__(self, game_manager, parent=None):
        super().__init__(parent)
        self.game_manager = game_manager

        self.setStyleSheet("""
                            QWidget {
                                background: rgb(60, 60, 60);
                            }
                            """)
        self.grid_layout = QGridLayout(self)
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.grid_layout.setSpacing(2)
        
        self.grid_layout.setColumnStretch(0, 4) 
        for i in range(1, 5):
            self.grid_layout.setColumnStretch(i, 2)

        self.stats = {}
    
    def add_spacer(self, row_index, height=16):
        spacer = QWidget()
        spacer.setMinimumHeight(height)
        self.grid_layout.addWidget(spacer, row_index, 0, 1, 5)

    def build_label(self, text, color=None):
        label = QLabel(text)
        label.setFont(DFont.SANS_REGULAR)
        label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        if color:
            label.setStyleSheet(f"color: {color};")
        return label

    def build(self):
        stats = self.game_manager.player.get_stats(DType.STR)
        skills = self.game_manager.player.get_skills(DType.STR)
        mastery = self.game_manager.player.get_mastery(DType.STR)
        row = 0
        
        self.add_spacer(row)
        row += 1
        for i in range(len(CharacterValues.STATS)):
            self.add_4_value(row, CharacterValues.STATS[i].upper(), stats[CharacterValues.STATS[i]][0], stats[CharacterValues.STATS[i]][1], stats[CharacterValues.STATS[i]][2], stats[CharacterValues.STATS[i]][3])
            row += 1
        
        self.add_spacer(row)
        row += 1
        for i in range(len(CharacterValues.SKILLS)):
            self.add_4_value(row, CharacterValues.SKILLS[i].upper(), skills[CharacterValues.SKILLS[i]][0], skills[CharacterValues.SKILLS[i]][1], skills[CharacterValues.SKILLS[i]][2], skills[CharacterValues.SKILLS[i]][3])
            row += 1

        self.add_spacer(row)
        row += 1
        for i in range(len(CharacterValues.MASTERY)):
            self.add_2_value(row, CharacterValues.MASTERY[i].upper(), mastery[CharacterValues.MASTERY[i]][0], mastery[CharacterValues.MASTERY[i]][1])
            row += 1

    def add_2_value(self, row_index, name, current, total):
        name_label = self.build_label(name, "white")
        name_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        
        current_label = self.build_label(f"{current}", "white")
        total_label = self.build_label(total, "white")
        
        self.grid_layout.addWidget(name_label, row_index, 0)
        self.grid_layout.addWidget(current_label, row_index, 3)
        self.grid_layout.addWidget(total_label, row_index, 4)

    def add_4_value(self, row_index, name, base, boost, penalty, total):
        name_label = self.build_label(name, "white")
        name_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        
        base_label = self.build_label(base)
        plus_label = self.build_label(f"+{boost}", "green")
        minus_label = self.build_label(f"-{penalty}", "red")
        total_label = self.build_label(total, "white")

        # Add to the Master Grid
        self.grid_layout.addWidget(name_label, row_index, 0)
        self.grid_layout.addWidget(base_label, row_index, 1)
        self.grid_layout.addWidget(plus_label, row_index, 2)
        self.grid_layout.addWidget(minus_label, row_index, 3)
        self.grid_layout.addWidget(total_label, row_index, 4)

        # Store references by name for easy updating
        self.stats[name] = {
            "base": base_label, "minus": minus_label, 
            "plus": plus_label, "total": total_label
        }
