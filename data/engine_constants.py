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
    ATTRIBUTES = ["rank", "location", "datetime", "hp", "kinetic resistance", "energy resistance", "chemical resistance"]
    STATS = ["vitality", "constitution", "strength", "agility", "dexterity", "perception", "intelligence", "rationality"]
    SKILLS = ["navigation", "stealth", "combat", "hunting", "recovery", "salvaging", "resources", "alchemy", "bartering", "lockpicking", "cryptography", "engineering", "gunsmithing", "bladecasting", "neuralforging", "armorcrafting"]
    MASTERY = ["carbines", "subcarbines", "lancers", "suppressors", "handcanons", "breachers", "launchers", "greatswords", "knives"]
