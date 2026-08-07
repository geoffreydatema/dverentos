from utils import *
from PySide6.QtWidgets import QWidget, QGridLayout, QVBoxLayout
from PySide6.QtCore import Qt
# from data.engine_constants import DFontSize
from engine.DScreen import DScreen
from engine.DGridContainer import DGridContainer
from engine.DVaultSlot import DVaultSlot
from engine.DInventorySlot import DInventorySlot
from engine.DComponentSlot import DComponentSlot
from engine.DWeaponSlot import DWeaponSlot
from engine.DToolSlot import DToolSlot
from engine.DStatus import DStatus
from engine.DCharacterNamePanel import DCharacterNamePanel
from engine.DCharacterValuesPanel import DCharacterValuesPanel
from engine.DCharacterAttributesPanel import DCharacterAttributesPanel
from engine.DInventoryPreviewPanel import DInventoryPreviewPanel
from engine.DStatusesPreviewPanel import DStatusesPreviewPanel
from engine.DCurrencyWidget import DCurrencyWidget

class DCharacterUI(DScreen):
    def __init__(self, parent=None, game_manager=None, image_path="assets/character_ui/character_ui_grid_v001.png"):
        super().__init__(parent, image_path)
        self.game_manager = game_manager

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
        self.name_layout.setContentsMargins(4, 4, 0, 4)
        self.grid_layout.addWidget(self.name_container, 0, 0, 2, 8)
        self.name_panel = DCharacterNamePanel(self.name_container)
        self.name_layout.addWidget(self.name_panel)
        self.name_panel.build()

        # attributes ==============================================================
        self.attributes_container = DGridContainer(2, 0)
        self.attributes_layout = QVBoxLayout(self.attributes_container)
        self.attributes_layout.setContentsMargins(4, 4, 0, 4)
        self.grid_layout.addWidget(self.attributes_container, 2, 0, 2, 5)
        self.attributes_panel = DCharacterAttributesPanel(self.attributes_container)
        self.attributes_layout.addWidget(self.attributes_panel)
        self.attributes_panel.build()

        # inventory preview =======================================================
        self.inventory_preview_container = DGridContainer(4, 0)
        self.inventory_preview_layout = QVBoxLayout(self.inventory_preview_container)
        self.inventory_preview_layout.setContentsMargins(4, 0, 0, 0)
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
        self.character_values_layout.setContentsMargins(4, 0, 1, 2)
        self.grid_layout.addWidget(self.character_values_container, 5, 0, 13, 4)
        self.character_value_panel = DCharacterValuesPanel(self.character_values_container, self.game_manager)
        self.character_values_layout.addWidget(self.character_value_panel)
        self.character_value_panel.build()

        # currency widgets ========================================================
        self.krezhna_widget = DCurrencyWidget()
        self.grid_layout.addWidget(self.krezhna_widget, 1, 28)

        self.currency2_widget = DCurrencyWidget()
        self.grid_layout.addWidget(self.currency2_widget, 1, 29)

        self.currency3_widget = DCurrencyWidget()
        self.grid_layout.addWidget(self.currency3_widget, 1, 30)

        self.currency4_widget = DCurrencyWidget()
        self.grid_layout.addWidget(self.currency4_widget, 1, 31)

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

        self.tensile_fibres = DComponentSlot(7, 9)
        self.grid_layout.addWidget(self.tensile_fibres, 7, 9)

        self.logic_registers = DComponentSlot(7, 14)
        self.grid_layout.addWidget(self.logic_registers, 7, 14)

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
        self.grid_layout.addWidget(self.vault_tab_container, 1, 24, 1, 4)
        for c in range(24, 32):
            for r in range(2, 18):
                slot = DVaultSlot(r, c)
                self.grid_layout.addWidget(slot, r, c)
                self.vault_slots[(r, c)] = slot

    def resizeEvent(self, event):
        super().resizeEvent(event)

        self.update_geometry()
