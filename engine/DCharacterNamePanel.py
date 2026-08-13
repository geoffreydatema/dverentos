from PySide6.QtWidgets import QWidget, QLabel, QGridLayout
from PySide6.QtCore import Qt
from engine.DFont import DFont

class DCharacterNamePanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setStyleSheet("""
                            QWidget {
                                background: rgb(60, 60, 60);
                                font-size: 40px;
                            }
                            """)
        self.grid_layout = QGridLayout(self)
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.grid_layout.setSpacing(4)
        
        self.grid_layout.setColumnStretch(0, 1) 
        self.grid_layout.setColumnStretch(1, 3) 

    def build_english_name(self):
        nameplate_rank_label = QLabel("0")
        nameplate_rank_label.setFont(DFont.SANS_LIGHT)
        nameplate_rank_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        english_name_label = QLabel("username")
        english_name_label.setFont(DFont.SANS_LIGHT)
        english_name_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        self.grid_layout.addWidget(nameplate_rank_label, 0, 0)
        self.grid_layout.addWidget(english_name_label, 0, 1)

    def build_tezhnor_name(self):
        tezhnor_rank_label = QLabel("0")
        tezhnor_rank_label.setFont(DFont.SANS_LIGHT)
        tezhnor_rank_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        tezhnor_name_label = QLabel("yპвэтэzнa")
        tezhnor_name_label.setFont(DFont.SERIF_LIGHT)
        tezhnor_name_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        self.grid_layout.addWidget(tezhnor_rank_label, 1, 0)
        self.grid_layout.addWidget(tezhnor_name_label, 1, 1)

    def build(self):
        self.build_english_name()
        self.build_tezhnor_name()
