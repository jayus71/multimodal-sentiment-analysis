import sys
import typing
from PyQt5 import QtCore

from PyQt5.QtCore import Qt, QTranslator, QLocale
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication,QMainWindow, QWidget

from test_ui import Ui_MainWindow

class testWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = testWindow()
    w.show()
    app.exec_()