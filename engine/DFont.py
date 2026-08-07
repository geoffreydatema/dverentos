from utils import *
from PySide6.QtGui import QFont

class DFont():
    SANS_LIGHT = QFont("Noto Sans")
    SANS_LIGHT.setWeight(QFont.Weight.Light)
    SANS_LIGHT.setPointSize(9)
    SANS_LIGHT.setStyleStrategy(QFont.StyleStrategy.PreferAntialias)
    SANS_LIGHT.setHintingPreference(QFont.HintingPreference.PreferNoHinting)

    SANS_REGULAR = QFont("Noto Sans")
    SANS_REGULAR.setWeight(QFont.Weight.Normal)
    SANS_REGULAR.setPointSize(9)
    SANS_REGULAR.setStyleStrategy(QFont.StyleStrategy.PreferAntialias)
    SANS_REGULAR.setHintingPreference(QFont.HintingPreference.PreferNoHinting)

    SANS_BOLD = QFont("Noto Sans")
    SANS_BOLD.setWeight(QFont.Weight.Bold)
    SANS_BOLD.setPointSize(9)
    SANS_BOLD.setStyleStrategy(QFont.StyleStrategy.PreferAntialias)
    SANS_BOLD.setHintingPreference(QFont.HintingPreference.PreferNoHinting)

    SERIF_LIGHT = QFont("Noto Serif")
    SERIF_LIGHT.setWeight(QFont.Weight.Light)
    SERIF_LIGHT.setPointSize(9)
    SERIF_LIGHT.setStyleStrategy(QFont.StyleStrategy.PreferAntialias)
    SERIF_LIGHT.setHintingPreference(QFont.HintingPreference.PreferNoHinting)

    SERIF_REGULAR = QFont("Noto Serif")
    SERIF_REGULAR.setWeight(QFont.Weight.Normal)
    SERIF_REGULAR.setPointSize(9)
    SERIF_REGULAR.setStyleStrategy(QFont.StyleStrategy.PreferAntialias)
    SERIF_REGULAR.setHintingPreference(QFont.HintingPreference.PreferNoHinting)

    SERIF_BOLD = QFont("Noto Serif")
    SERIF_BOLD.setWeight(QFont.Weight.Bold)
    SERIF_BOLD.setPointSize(9) 
    SERIF_BOLD.setStyleStrategy(QFont.StyleStrategy.PreferAntialias)
    SERIF_BOLD.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
