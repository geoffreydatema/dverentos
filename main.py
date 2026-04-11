import sys
from PySide6.QtWidgets import QApplication, QMainWindow

class Dverentos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DVERENTOS")
        self.setGeometry(0, 0, 1280, 720)

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = Dverentos()
    window.show()
    sys.exit(application.exec())
