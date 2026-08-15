from utils import *
from PySide6.QtWidgets import QWidget
from engine.DScreen import DScreen

class DCraftingUI(DScreen):
    def __init__(self, parent: QWidget, image_path: str="assets/placeholder/crafting_placeholder_v001.jpg") -> None:
        super().__init__(parent, image_path)
