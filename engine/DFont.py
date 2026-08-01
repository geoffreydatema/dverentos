from utils import *
from PySide6.QtGui import QFont

class DFont():
    SANS_LIGHT = QFont("Noto Sans")
    SANS_LIGHT.setWeight(QFont.Weight.Light)

    SANS_REGULAR = QFont("Noto Sans")
    SANS_REGULAR.setWeight(QFont.Weight.Normal)

    SANS_BOLD = QFont("Noto Sans")
    SANS_BOLD.setWeight(QFont.Weight.Bold)

    SERIF_LIGHT = QFont("Noto Serif")
    SERIF_LIGHT.setWeight(QFont.Weight.Light)

    SERIF_REGULAR = QFont("Noto Serif")
    SERIF_REGULAR.setWeight(QFont.Weight.Normal)

    SERIF_BOLD = QFont("Noto Serif")
    SERIF_BOLD.setWeight(QFont.Weight.Bold)
