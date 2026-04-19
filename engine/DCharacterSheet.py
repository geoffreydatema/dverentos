from utils import *
from PySide6.QtWidgets import QVBoxLayout
from engine.DScreen import DScreen

class DCharacterSheet(DScreen):
    def __init__(self, parent=None, engine_manager=None, image_path="assets/placeholder/character_placeholder_v001.jpg"):
        super().__init__(parent, image_path)
