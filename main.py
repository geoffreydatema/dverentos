from utils import *
import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFontDatabase, QFont
from engine import Dverentos

def load_all_fonts(font_dir: Path) -> str:
    """Registers all .ttf files in a directory and returns the primary family name."""
    family_name = ""
    
    if not font_dir.exists():
        print(f"Warning: Font directory '{font_dir}' does not exist.")
        return ""

    for ttf_file in font_dir.glob("*.ttf"):
        font_id = QFontDatabase.addApplicationFont(str(ttf_file))
        
        if font_id == -1:
            print(f"Failed to load font: {ttf_file.name}")
        else:
            families = QFontDatabase.applicationFontFamilies(font_id)
            if families and not family_name:
                family_name = families[0]

    return family_name

if __name__ == "__main__":
    from engine.DFont import DFont

    application = QApplication(sys.argv)
    fonts_directory = Path(__file__).parent / "assets" / "fonts"
    font_family = load_all_fonts(fonts_directory)

    if font_family:
        application.setFont(DFont.SANS_REGULAR)
        
    window = Dverentos()
    window.show()
    sys.exit(application.exec())
