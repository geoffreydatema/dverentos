from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine.Dverentos import Dverentos

from utils import *
from PySide6.QtCore import QCoreApplication

class DEngineManager():
    def __init__(self, engine: Dverentos) -> None:
        self.engine = engine
        self.commands = [
            "quit"
        ]
        self.settings: dict[str, bool | tuple[int, int]] = {
            "resolution": (1280, 720),
            "fullscreen": False,
            "fullscreen_windowed": False
        }

    def apply_settings(self) -> None:
        # start in half res windowed
        # self.set_resolution(self.settings.get("resolution")[0], self.settings.get("resolution")[1])
        
        # start in fullscreen
        self.set_fullscreen("true")

    def quit(self) -> None:
        info("Exiting now")
        QCoreApplication.quit()

    def set_resolution(self, w: int, h: int) -> None:
        width = w
        height = h
        
        self.engine.update_geometry(w=width, h=height)
        info(f"Resolution set to {width} x {height}")

    def set_fullscreen(self, value: str) -> None:
        if value == "true":
            self.engine.update_geometry(fullscreen=True)
            info("Application set to fullscreen")
        elif value == "false":
            self.engine.update_geometry(fullscreen_windowed=True)
            info("Application set to fullscreen windowed")
        else:
            error('Fullscreen arg must be "true" or "false"')
            return
        
    def set_fullscreen_windowed(self, value: str) -> None:
        if value == "true":
            self.engine.update_geometry(fullscreen_windowed=True)
            info("Application set to fullscreen windowed")
        elif value == "false":
            self.engine.update_geometry(fullscreen=True)
            info("Application set to fullscreen")
        else:
            error('Fullscreen arg must be "true" or "false"')
            return
