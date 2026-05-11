from enum import IntEnum, auto

class DType(IntEnum):
    INT = auto()
    STR = auto()

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

class CharacterValues():
    ATTRIBUTES = ["rank", "location", "コᴋ datetime", "hp", "kinetic resistance", "energy resistance", "chemical resistance"]
    STATS = ["vitality", "constitution", "agility", "dexterity", "perception", "rationality"]
    SKILLS = ["salvaging", "harvesting", "hunting", "mining", "lockpicking", "cryptography", "engineering", "stealth", "alchemy", "weaponcrafting", "toolsmithing", "neuralforging"]
    MASTERY = ["light melee", "heavy melee", "hand cannons", "big guns", "energy", "telekinesis"]
