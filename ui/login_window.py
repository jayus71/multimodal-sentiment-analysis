# import os
# import sys
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget
# from Ui_login import Ui_login



# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     mainWindow = QMainWindow()
#     Ui_login_window = Ui_login()
#     Ui_login_window.setupUi(mainWindow)
#     mainWindow.show()
#     sys.exit(app.exec_())

import sys
import random
from PyQt5.QtWidgets import *
import pyqtgraph as pg

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建一个Qt图形窗口
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        # 设置图表坐标轴标签
        self.graphWidget.setLabel('left', 'Accuracy')
        self.graphWidget.setLabel('bottom', 'Iterations')

        # 创建一个空的数据曲线
        self.data_line = self.graphWidget.plot(pen=pg.mkPen('b', width=2))
        self.x = []
        self.y = []

        # 模拟数据更新
        self.timer = pg.QtCore.QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(1000)  # 每秒钟更新一次数据

    def update_plot(self):
        # 模拟随机生成一个accuracy值
        accuracy = random.random()

        # 将新的数据添加到曲线中
        self.x.append(len(self.x))
        self.y.append(accuracy)

        # 更新数据曲线
        self.data_line.setData(self.x, self.y)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    