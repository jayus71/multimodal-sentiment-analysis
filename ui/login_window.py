import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget
from Ui_login import Ui_login



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    Ui_login_window = Ui_login()
    Ui_login_window.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

    