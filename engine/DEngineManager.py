from utils import *
from PySide6.QtCore import QCoreApplication

class DEngineManager():
    def __init__(self, engine=None):
        self.engine = engine
        self.commands = [
            "quit"
        ]
        self.settings = {
            "resolution": (1280, 720),
            "fullscreen": False,
            "fullscreen_windowed": False
        }

    def apply_settings(self):
        # start in half res windowed
        self.set_resolution(self.settings.get("resolution")[0], self.settings.get("resolution")[1])
        
        # start in fullscreen
        # self.set_fullscreen("true")

    def quit(self):
        info("Exiting now")
        QCoreApplication.quit()

    def set_resolution(self, w, h):
        try:
            width = int(w)
            height = int(h)
        except ValueError:
            error("Resolution args must be int")
            return
        
        self.engine.update_geometry(w=width, h=height)
        info(f"Resolution set to {width} x {height}")

    def set_fullscreen(self, value):
        if value == "true":
            self.engine.update_geometry(fullscreen=True)
            info("Application set to fullscreen")
        elif value == "false":
            self.engine.update_geometry(fullscreen_windowed=True)
            info("Application set to fullscreen windowed")
        else:
            error('Fullscreen arg must be "true" or "false"')
            return
        
    def set_fullscreen_windowed(self, value):
        if value == "true":
            self.engine.update_geometry(fullscreen_windowed=True)
            info("Application set to fullscreen windowed")
        elif value == "false":
            self.engine.update_geometry(fullscreen=True)
            info("Application set to fullscreen")
        else:
            error('Fullscreen arg must be "true" or "false"')
            return
