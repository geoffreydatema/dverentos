from PySide6.QtWidgets import QWidget, QLabel, QGridLayout
from PySide6.QtCore import Qt

class DCharacterAttributesPanel(QWidget):
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
        
        self.layout.setColumnStretch(0, 1) 
        self.layout.setColumnStretch(1, 1) 

        self.attributes = {}
        self.stats = {}

    def build_rank(self):
        name_label = QLabel("RANK")
        name_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        value_label = QLabel("0")
        value_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.layout.addWidget(name_label, 0, 0)
        self.layout.addWidget(value_label, 0, 1)
        self.attributes["rank"] = value_label

    def build_location(self):
        name_label = QLabel("LOCATION")
        name_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        value_label = QLabel("<DESTINATION> [0, 0]")
        value_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.layout.addWidget(name_label, 1, 0)
        self.layout.addWidget(value_label, 1, 1)
        self.attributes["location"] = value_label

    def build_date(self):
        name_label = QLabel("コᴋ DATETIME")
        name_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        value_label = QLabel("00:00:00|00:00:00")
        value_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.layout.addWidget(name_label, 2, 0)
        self.layout.addWidget(value_label, 2, 1)
        self.attributes["date"] = value_label
        
    def build_hp(self):
        name_label = QLabel("HP")
        name_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        value_label = QLabel("0")
        value_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.layout.addWidget(name_label, 3, 0)
        self.layout.addWidget(value_label, 3, 1)
        self.attributes["hp"] = value_label

    def build_kinetic_resistance(self):
        name_label = QLabel("KINETIC RESISTANCE")
        name_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        value_label = QLabel("9999")
        value_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.layout.addWidget(name_label, 4, 0)
        self.layout.addWidget(value_label, 4, 1)
        self.attributes["kinetic_resistance"] = value_label

    def build_energy_resistance(self):
        name_label = QLabel("ENERGY RESISTANCE")
        name_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        value_label = QLabel("9999")
        value_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.layout.addWidget(name_label, 5, 0)
        self.layout.addWidget(value_label, 5, 1)
        self.attributes["energy_resistance"] = value_label

    def build_chemical_resistance(self):
        name_label = QLabel("CHEMICAL RESISTANCE")
        name_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        value_label = QLabel("9999")
        value_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.layout.addWidget(name_label, 6, 0)
        self.layout.addWidget(value_label, 6, 1)
        self.attributes["chemical_resistance"] = value_label

    def build(self):
        self.build_rank()
        self.build_location()
        self.build_date()
        self.build_hp()
        self.build_kinetic_resistance()
        self.build_energy_resistance()
        self.build_chemical_resistance()
