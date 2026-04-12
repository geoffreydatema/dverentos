import sys
from PySide6.QtWidgets import QApplication
from engine import Dverentos

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = Dverentos()
    window.show()
    sys.exit(application.exec())
