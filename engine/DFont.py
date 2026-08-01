from utils import *
from PySide6.QtGui import QFont

class DFont():
    SANS_LIGHT = QFont("Noto Sans")
    SANS_LIGHT.setWeight(QFont.Weight.Light)
    SANS_LIGHT.setPointSize(10)

    SANS_REGULAR = QFont("Noto Sans")
    SANS_REGULAR.setWeight(QFont.Weight.Normal)
    SANS_REGULAR.setPointSize(10)

    SANS_BOLD = QFont("Noto Sans")
    SANS_BOLD.setWeight(QFont.Weight.Bold)
    SANS_BOLD.setPointSize(10)

    SERIF_LIGHT = QFont("Noto Serif")
    SERIF_LIGHT.setWeight(QFont.Weight.Light)
    SERIF_LIGHT.setPointSize(10)

    SERIF_REGULAR = QFont("Noto Serif")
    SERIF_REGULAR.setWeight(QFont.Weight.Normal)
    SERIF_REGULAR.setPointSize(10)

    SERIF_BOLD = QFont("Noto Serif")
    SERIF_BOLD.setWeight(QFont.Weight.Bold)
    SERIF_BOLD.setPointSize(10)
