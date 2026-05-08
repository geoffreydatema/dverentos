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

    def build_damage_resistance(self):
        name_label = QLabel("DAMAGE RESISTANCE")
        name_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        value_label = QLabel("0")
        value_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.layout.addWidget(name_label, 4, 0)
        self.layout.addWidget(value_label, 4, 1)
        self.attributes["damage_resistance"] = value_label

    def build_status_resistance(self):
        name_label = QLabel("STATUS RESISTANCE")
        name_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        value_label = QLabel("0")
        value_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.layout.addWidget(name_label, 5, 0)
        self.layout.addWidget(value_label, 5, 1)
        self.attributes["status_resistance"] = value_label

    def build(self):
        self.build_rank()
        self.build_location()
        self.build_date()
        self.build_hp()
        self.build_damage_resistance()
        self.build_status_resistance()
        # name_label = QLabel(name)
        # name_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        
        # base_label = self.create_val_label("999")
        # minus_label = self.create_val_label("-999", "red")
        # plus_label = self.create_val_label("+999", "green")
        # total_label = self.create_val_label("999", "white")

        # # Add to the Master Grid
        # self.layout.addWidget(name_label, row_index, 0)
        # self.layout.addWidget(base_label, row_index, 1)
        # self.layout.addWidget(minus_label, row_index, 2)
        # self.layout.addWidget(plus_label, row_index, 3)
        # self.layout.addWidget(total_label, row_index, 4)

        # # Store references by name for easy updating
        # self.stats[name] = {
        #     "base": base_label, "minus": minus_label, 
        #     "plus": plus_label, "total": total_label
        # }

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
