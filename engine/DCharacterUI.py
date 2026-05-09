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
from engine.DCharacterNamePanel import DCharacterNamePanel
from engine.DCharacterValuePanel import DCharacterValuePanel
from engine.DCharacterAttributesPanel import DCharacterAttributesPanel
from engine.DInventoryPreviewPanel import DInventoryPreviewPanel
from engine.DStatusesPreviewPanel import DStatusesPreviewPanel
from engine.DCurrencyWidget import DCurrencyWidget

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
        
        # name plate ==============================================================
        self.name_container = DGridContainer(0, 0)
        self.name_layout = QVBoxLayout(self.name_container)
        self.name_layout.setContentsMargins(8, 4, 0, 4)
        self.grid_layout.addWidget(self.name_container, 0, 0, 2, 8)

        self.name_panel = DCharacterNamePanel(self.name_container)
        self.name_layout.addWidget(self.name_panel)
        self.name_panel.build()

        # attributes ==============================================================
        self.attributes_container = DGridContainer(2, 0)
        self.attributes_layout = QVBoxLayout(self.attributes_container)
        self.attributes_layout.setContentsMargins(8, 4, 0, 4)
        self.grid_layout.addWidget(self.attributes_container, 2, 0, 2, 5)

        self.attributes_panel = DCharacterAttributesPanel(self.attributes_container)
        self.attributes_layout.addWidget(self.attributes_panel)
        self.attributes_panel.build()

        # inventory preview =======================================================
        self.inventory_preview_container = DGridContainer(4, 0)
        self.inventory_preview_layout = QVBoxLayout(self.inventory_preview_container)
        self.inventory_preview_layout.setContentsMargins(8, 0, 0, 0)
        self.grid_layout.addWidget(self.inventory_preview_container, 4, 0, 1, 4)

        self.inventory_preview_panel = DInventoryPreviewPanel(self.inventory_preview_container)
        self.inventory_preview_layout.addWidget(self.inventory_preview_panel)
        self.inventory_preview_panel.build()

        # statuses preview ========================================================
        self.statuses_preview_container = DGridContainer(4, 4)
        self.statuses_preview_layout = QVBoxLayout(self.statuses_preview_container)
        self.statuses_preview_layout.setContentsMargins(0, 0, 0, 0)
        self.grid_layout.addWidget(self.statuses_preview_container, 4, 4, 1, 1)

        self.statuses_preview_panel = DStatusesPreviewPanel(self.statuses_preview_container)
        self.statuses_preview_layout.addWidget(self.statuses_preview_panel)
        self.statuses_preview_panel.build()

        # character values ========================================================
        self.character_values_container = DGridContainer(5, 0)
        self.character_values_layout = QVBoxLayout(self.character_values_container)
        self.character_values_layout.setContentsMargins(8, 0, 1, 10)
        self.grid_layout.addWidget(self.character_values_container, 5, 0, 13, 4)

        self.character_value_panel = DCharacterValuePanel(self.character_values_container)
        self.character_values_layout.addWidget(self.character_value_panel)

        r = 0
        self.character_value_panel.add_spacer(r)
        r += 1

        for stat in ["VITALITY", "CONSTITUTION", "AGILITY", "DEXTERITY", "PERCEPTION", "RATIONALITY"]:
            self.character_value_panel.add_stat_row(r, stat)
            r += 1

        self.character_value_panel.add_spacer(r)
        r += 1

        for skill in ["SALVAGING", "HARVESTING", "HUNTING", "MINING", "LOCKPICKING", 
                    "CRYPTOGRAPHY", "ENGINEERING", "STEALTH", "ALCHEMY", 
                    "WEAPONCRAFTING", "TOOLSMITHING", "NEURALFORGING"]:
            self.character_value_panel.add_stat_row(r, skill)
            r += 1

        self.character_value_panel.add_spacer(r)
        r += 1

        for mastery in ["LIGHT MELEE", "HEAVY MELEE", "HAND CANNONS", "BIG GUNS", "ENERGY", "TELEKINESIS"]:
            self.character_value_panel.add_stat_row(r, mastery)
            r += 1

        # currency widgets ========================================================
        self.krezhna_widget = DCurrencyWidget()
        self.grid_layout.addWidget(self.krezhna_widget, 1, 15)

        self.currency2_widget = DCurrencyWidget()
        self.grid_layout.addWidget(self.currency2_widget, 1, 16)

        self.currency3_widget = DCurrencyWidget()
        self.grid_layout.addWidget(self.currency3_widget, 1, 17)

        self.currency4_widget = DCurrencyWidget()
        self.grid_layout.addWidget(self.currency4_widget, 1, 18)

        # component slots =========================================================
        self.sensors_slot = DComponentSlot(3, 9)
        self.grid_layout.addWidget(self.sensors_slot, 3, 9)

        self.neural_network = DComponentSlot(3, 14)
        self.grid_layout.addWidget(self.neural_network, 3, 14)

        self.reactor_core = DComponentSlot(4, 11)
        self.grid_layout.addWidget(self.reactor_core, 4, 11)

        self.nano_fibres = DComponentSlot(5, 9)
        self.grid_layout.addWidget(self.nano_fibres, 5, 9)

        self.actuators = DComponentSlot(5, 14)
        self.grid_layout.addWidget(self.actuators, 5, 14)

        self.power_transport = DComponentSlot(6, 12)
        self.grid_layout.addWidget(self.power_transport, 6, 12)

        # weapon slots ============================================================
        self.primary_weapon_slot = DWeaponSlot(11, 5)
        self.grid_layout.addWidget(self.primary_weapon_slot, 11, 6, 2, 5)

        self.secondary_weapon_slot = DWeaponSlot(11, 12)
        self.grid_layout.addWidget(self.secondary_weapon_slot, 11, 12, 2, 5)

        # statuses ================================================================
        self.statuses = {}
        for c in range(6, 10):
            for r in range(14, 18):
                status = DStatus(r, c)
                self.grid_layout.addWidget(status, r, c)
                self.statuses[(r, c)] = status

        # tools ===================================================================
        self.scanner = DToolSlot(14, 13)
        self.grid_layout.addWidget(self.scanner, 14, 13)

        self.harvesting_knife = DToolSlot(14, 14)
        self.grid_layout.addWidget(self.harvesting_knife, 14, 14)

        self.hunting_javelin = DToolSlot(14, 15)
        self.grid_layout.addWidget(self.hunting_javelin, 14, 15)

        self.mining_laser = DToolSlot(14, 16)
        self.grid_layout.addWidget(self.mining_laser, 14, 16)

        # character sheet inventory ===============================================
        self.inventory_slots = {}
        self.carry_weight_container = DGridContainer(1, 19)
        self.grid_layout.addWidget(self.carry_weight_container, 1, 19, 1, 4)
        for c in range(19, 23):
            for r in range(2, 18):
                slot = DInventorySlot(r, c)
                self.grid_layout.addWidget(slot, r, c)
                self.inventory_slots[(r, c)] = slot

        # character sheet vault ===================================================
        self.vault_slots = {}
        self.vault_tab_container = DGridContainer(1, 24)
        self.grid_layout.addWidget(self.vault_tab_container, 1, 24, 1, 8)
        for c in range(24, 32):
            for r in range(2, 18):
                slot = DVaultSlot(r, c)
                self.grid_layout.addWidget(slot, r, c)
                self.vault_slots[(r, c)] = slot

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
