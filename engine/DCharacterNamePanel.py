from PySide6.QtWidgets import QWidget, QLabel, QGridLayout
from PySide6.QtCore import Qt

class DCharacterNamePanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setStyleSheet("""
                            QWidget {
                                background: rgb(60, 60, 60);
                                font-size: 40px;
                            }
                            """)
        self.layout = QGridLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(4)
        
        self.layout.setColumnStretch(0, 1) 
        self.layout.setColumnStretch(1, 3) 

    def build_english_name(self):
        nameplate_rank_label = QLabel("0")
        nameplate_rank_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        english_name_label = QLabel("username")
        english_name_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.layout.addWidget(nameplate_rank_label, 0, 0)
        self.layout.addWidget(english_name_label, 0, 1)

    def build_angloslav_name(self):
        angloslav_rank_label = QLabel("0")
        angloslav_rank_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        angloslav_name_label = QLabel("hゼラнλм")
        angloslav_name_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.layout.addWidget(angloslav_rank_label, 1, 0)
        self.layout.addWidget(angloslav_name_label, 1, 1)

    def build(self):
        self.build_english_name()
        self.build_angloslav_name()
