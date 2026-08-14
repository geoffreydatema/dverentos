from utils import *
from engine.DScreen import DScreen

class DArchiveUI(DScreen):
    def __init__(self, parent=None, engine_manager=None, image_path="assets/placeholder/archive_placeholder_v001.jpg"):
        super().__init__(parent, image_path)
