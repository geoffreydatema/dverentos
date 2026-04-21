from utils import *
from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QFrame, QSizePolicy, QVBoxLayout
from PySide6.QtCore import Qt
from data.engine_constants import DFontSize
from engine.DScreen import DScreen
from engine.DGridContainer import DGridContainer
from engine.DVaultSlot import DVaultSlot
from engine.DInventorySlot import DInventorySlot
from engine.DComponentSlot import DComponentSlot
from engine.DWeaponSlot import DWeaponSlot
from engine.DToolSlot import DToolSlot
from engine.DStatus import DStatus

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

        # character sheet vault
        self.vault_slots = {}
        self.vault_tab_container = DGridContainer(1, 24)
        self.grid_layout.addWidget(self.vault_tab_container, 1, 24, 1, 8)
        for c in range(24, 32):
            for r in range(2, 18):
                slot = DVaultSlot(r, c)
                self.grid_layout.addWidget(slot, r, c)
                self.vault_slots[(r, c)] = slot

        # character sheet inventory
        self.inventory_slots = {}
        self.carry_weight_container = DGridContainer(1, 19)
        self.grid_layout.addWidget(self.carry_weight_container, 1, 19, 1, 4)
        for c in range(19, 23):
            for r in range(2, 18):
                slot = DInventorySlot(r, c)
                self.grid_layout.addWidget(slot, r, c)
                self.vault_slots[(r, c)] = slot

        # component slots
        self.sensors_slot = DComponentSlot(3, 8)
        self.grid_layout.addWidget(self.sensors_slot, 3, 8)

        self.neural_network = DComponentSlot(3, 13)
        self.grid_layout.addWidget(self.neural_network, 3, 13)

        self.reactor_core = DComponentSlot(4, 10)
        self.grid_layout.addWidget(self.reactor_core, 4, 10)

        self.nano_fibres = DComponentSlot(5, 8)
        self.grid_layout.addWidget(self.nano_fibres, 5, 8)

        self.actuators = DComponentSlot(5, 13)
        self.grid_layout.addWidget(self.actuators, 5, 13)

        self.power_transport = DComponentSlot(6, 11)
        self.grid_layout.addWidget(self.power_transport, 6, 11)

        # weapon slots
        self.primary_weapon_slot = DWeaponSlot(12, 5)
        self.grid_layout.addWidget(self.primary_weapon_slot, 12, 5, 2, 5)

        self.secondary_weapon_slot = DWeaponSlot(12, 12)
        self.grid_layout.addWidget(self.secondary_weapon_slot, 12, 12, 2, 5)

        # statuses
        self.statuses = {}
        for c in range(5, 9):
            for r in range(15, 18):
                status = DStatus(r, c)
                self.grid_layout.addWidget(status, r, c)
                self.statuses[(r, c)] = status

        # tools
        self.scanner = DToolSlot(16, 13)
        self.grid_layout.addWidget(self.scanner, 16, 13)

        self.harvesting_knife = DToolSlot(16, 14)
        self.grid_layout.addWidget(self.harvesting_knife, 16, 14)

        self.hunting_javelin = DToolSlot(16, 15)
        self.grid_layout.addWidget(self.hunting_javelin, 16, 15)

        self.mining_laser = DToolSlot(16, 16)
        self.grid_layout.addWidget(self.mining_laser, 16, 16)
        
        # character values
        self.character_values_container = DGridContainer(5, 0)
        self.grid_layout.addWidget(self.character_values_container, 5, 0, 13, 3)

        # name plate
        self.name_plate_container = DGridContainer(0, 0)
        self.grid_layout.addWidget(self.name_plate_container, 0, 0, 2, 8)

        # attributes
        self.attributes_container = DGridContainer(2, 0)
        self.grid_layout.addWidget(self.attributes_container, 2, 0, 1, 4)

        # inventory preview
        self.inventory_preview_container = DGridContainer(3, 0)
        self.grid_layout.addWidget(self.inventory_preview_container, 3, 0, 1, 4)

        # statuses preview
        self.statuses_preview_container = DGridContainer(3, 4)
        self.grid_layout.addWidget(self.statuses_preview_container, 3, 4, 1, 1)

        #===================================================================================
        #@! general idea for a text wrapper
        # self.label_wrapper = QFrame()
        # self.label_wrapper.setStyleSheet("background: rgb(30, 30, 30); border: none;")
        # self.label_wrapper.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        
        # wrapper_layout = QVBoxLayout(self.label_wrapper)
        # wrapper_layout.setContentsMargins(0, 0, 0, 0)
        # wrapper_layout.setSpacing(0)

        # self.label = QLabel("STAT PLACEHOLDER")
        # self.label.setAlignment(Qt.AlignCenter)
        # self.label.setStyleSheet("color: white; background: transparent;")
        
        # wrapper_layout.addWidget(self.label)
        # self.grid_layout.addWidget(self.label_wrapper, 5, 2, 1, 3)

    def resizeEvent(self, event):
        super().resizeEvent(event)

        self.update_geometry()
        
    def update_geometry(self):
        # @! likely we will move this function (and possibly update_fonts) as well to DScreen if most of it can be inherited

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
        
        # font = self.label.font()
        # font.setPixelSize(new_size)
        # self.label.setFont(font)
