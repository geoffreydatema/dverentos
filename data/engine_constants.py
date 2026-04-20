from enum import IntEnum, auto

class DScreenID(IntEnum):
    MAIN_MENU = auto()
    PLACEHOLDER = auto()
    CHARACTER = auto()
    VAULT = auto()
    CRAFTING = auto()
    ARCHIVE = auto()

class DFontSize():
    ACCOUNT_UI_NAVBAR = 0.25
    CHARACTER_UI_STATS = 0.3
