import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from ui_braincorr import Ui_MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
