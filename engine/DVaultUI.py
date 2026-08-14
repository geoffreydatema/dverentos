from utils import *
from engine.DScreen import DScreen

class DVaultUI(DScreen):
    def __init__(self, parent=None, engine_manager=None, image_path="assets/placeholder/vault_placeholder_v001.jpg"):
        super().__init__(parent, image_path)
