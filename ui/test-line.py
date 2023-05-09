# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow,QVBoxLayout, QPushButton,QWidget
# from PyQt5.QtChart import QChart, QChartView, QLineSeries, QValueAxis
# from PyQt5.QtCore import Qt, QPointF
# from PyQt5 import QtGui 



# class LossAccuracyPlot(QMainWindow):
#     def __init__(self, loss_data, accuracy_data):
#         super().__init__()

#         self.loss_data = loss_data
#         self.accuracy_data = accuracy_data

#         self.init_ui()

#     def init_ui(self):
#         self.setWindowTitle('Loss and Accuracy Plot')

#         main_layout = QVBoxLayout()

#         self.chart_view = self.create_chart_view()

#         update_button = QPushButton("Update Data")
#         update_button.clicked.connect(self.update_data)

#         main_layout.addWidget(self.chart_view)
#         main_layout.addWidget(update_button)

#         central_widget = QWidget()
#         central_widget.setLayout(main_layout)

#         self.setCentralWidget(central_widget)
#         self.resize(800, 600)

#     def create_chart_view(self):
#         series_loss = QLineSeries()
#         series_accuracy = QLineSeries()

#         chart = self.create_chart(series_loss, series_accuracy)

#         chart_view = QChartView(chart)
#         chart_view.setRenderHint(QtGui.QPainter.Antialiasing)

#         return chart_view

#     def create_chart(self, series_loss, series_accuracy):
#         for i, (loss, accuracy) in enumerate(zip(self.loss_data, self.accuracy_data), start=1):
#             series_loss.append(QPointF(i, loss))
#             series_accuracy.append(QPointF(i, accuracy))

#         chart = QChart()
#         chart.addSeries(series_loss)
#         chart.addSeries(series_accuracy)

#         chart.setTitle('Loss and Accuracy Plot')
#         chart.createDefaultAxes()

#         chart.legend().setAlignment(Qt.AlignBottom)
#         series_loss.setName('Loss')
#         series_accuracy.setName('Accuracy')

#         return chart

#     def update_data(self):
#         # 模拟更新数据
#         self.loss_data.append(self.loss_data[-1] - 0.1)
#         self.accuracy_data.append(self.accuracy_data[-1] + 0.1)

#         # 删除旧的折线图
#         old_chart_view = self.chart_view
#         self.chart_view = self.create_chart_view()
#         old_chart_view.deleteLater()

#         # 更新界面上的折线图
#         layout = self.centralWidget().layout()
#         layout.insertWidget(0, self.chart_view)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)

#     # 示例数据
#     loss_data = [1, 0.8, 0.6, 0.4, 0.2]
#     accuracy_data = [0.5, 0.6, 0.7, 0.8, 0.85]

#     main_window = LossAccuracyPlot(loss_data, accuracy_data)
#     main_window.show()

#     sys.exit(app.exec_())


# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
# from PyQt5.QtChart import QChart, QChartView, QLineSeries
# from PyQt5.QtGui import QPen
# from PyQt5.QtCore import Qt
# from PyQt5 import QtGui 

# class MyWindow(QMainWindow):
#     def __init__(self, loss_array, acc_array):
#         super().__init__()

#         self.setWindowTitle('Loss and Accuracy Graph')
#         self.setGeometry(100, 100, 800, 600)

#         # 设置中心窗口，用于显示图形
#         central_widget = QWidget(self)
#         self.setCentralWidget(central_widget)

#         # 创建绘图区域
#         chart = QChart()
#         chart.setTheme(QChart.ChartThemeLight)
#         chart.setTitle('Loss and Accuracy Graph')

#         # 创建数据序列
#         loss_series = QLineSeries()
#         loss_series.setName('Loss')
#         for i in range(len(loss_array)):
#             loss_series.append(i, loss_array[i])

#         acc_series = QLineSeries()
#         acc_series.setName('Accuracy')
#         for i in range(len(acc_array)):
#             acc_series.append(i, acc_array[i])

#         # 设置数据序列的画笔
#         loss_pen = QPen(Qt.red)
#         loss_pen.setWidth(2)
#         loss_series.setPen(loss_pen)

#         acc_pen = QPen(Qt.blue)
#         acc_pen.setWidth(2)
#         acc_series.setPen(acc_pen)

#         # 添加数据序列到图表中
#         chart.addSeries(loss_series)
#         chart.addSeries(acc_series)

#         # 设置x、y轴标签和网格线
#         chart.createDefaultAxes()
#         chart.axes(Qt.Horizontal)[0].setTitleText('Epoch')
#         chart.axes(Qt.Vertical)[0].setTitleText('Value')
#         chart.axes(Qt.Vertical)[0].setGridLineVisible(True)
#         chart.axes(Qt.Horizontal)[0].setGridLineVisible(True)

#         # 将图表添加到QChartView中
#         chart_view = QChartView(chart)
#         chart_view.setRenderHint(QtGui.QPainter.Antialiasing)
#         chart_view.setRubberBand(QChartView.HorizontalRubberBand)

#         # 将QChartView添加到窗口中心区域
#         v_layout = QVBoxLayout(central_widget)
#         v_layout.addWidget(chart_view)
#         self.setLayout(v_layout)


# if __name__ == '__main__':
#     app = QApplication(sys.argv)

#     # 生成测试数据，将其替换为您的实际数据
#     loss = [0.7, 0.6, 0.4, 0.3, 0.2, 0.15, 0.1, 0.08, 0.05, 0.02]
#     acc = [0.5, 0.6, 0.7, 0.8, 0.85, 0.9, 0.92, 0.94, 0.96, 0.98]

#     # 创建并显示主窗口
#     my_window = MyWindow(loss, acc)
#     my_window.show()

#     sys.exit(app.exec_())



import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget,QComboBox,QPushButton,QHBoxLayout
from PyQt5.QtChart import QChart, QChartView, QLineSeries
from PyQt5.QtGui import QPen, QPainter
from PyQt5.QtCore import Qt,QThread
import time


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Loss and Accuracy Graph')
        self.setGeometry(100, 100, 800, 600)

        # 设置中心窗口，用于显示图形
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # 创建数据系列
        self.loss_series = QLineSeries()
        self.loss_series.setName('Loss')

        self.acc_series = QLineSeries()
        self.acc_series.setName('Accuracy')

        # 添加新区域
        self.loss_series_2 = QLineSeries()
        self.loss_series_2.setName('Loss 2')

        self.acc_series_2 = QLineSeries()
        self.acc_series_2.setName('Accuracy 2')

        self.chart_2 = QChart()
        self.chart_2.setTheme(QChart.ChartThemeLight)
        self.chart_2.setTitle('Graph 2')

        loss_pen_2 = QPen(Qt.green)
        loss_pen_2.setWidth(2)
        self.loss_series_2.setPen(loss_pen_2)

        acc_pen_2 = QPen(Qt.magenta)
        acc_pen_2.setWidth(2)
        self.acc_series_2.setPen(acc_pen_2)

        self.chart_2.addSeries(self.loss_series_2)
        self.chart_2.addSeries(self.acc_series_2)

        self.chart_2.createDefaultAxes()
        self.chart_2.axes(Qt.Horizontal)[0].setTitleText('Epoch')
        self.chart_2.axes(Qt.Vertical)[0].setTitleText('Value')
        self.chart_2.axes(Qt.Vertical)[0].setGridLineVisible(True)
        self.chart_2.axes(Qt.Horizontal)[0].setGridLineVisible(True)

        # 创建绘图区域
        self.chart = QChart()
        self.chart.setTheme(QChart.ChartThemeLight)
        self.chart.setTitle('Loss and Accuracy Graph')

        # 设置数据序列的画笔
        loss_pen = QPen(Qt.red)
        loss_pen.setWidth(2)
        self.loss_series.setPen(loss_pen)

        acc_pen = QPen(Qt.blue)
        acc_pen.setWidth(2)
        self.acc_series.setPen(acc_pen)

        # 添加数据序列到图表中
        self.chart.addSeries(self.loss_series)
        self.chart.addSeries(self.acc_series)

        # 设置x、y轴标签和网格线
        self.chart.createDefaultAxes()
        self.chart.axes(Qt.Horizontal)[0].setTitleText('Epoch')
        self.chart.axes(Qt.Vertical)[0].setTitleText('Value')
        self.chart.axes(Qt.Vertical)[0].setGridLineVisible(True)
        self.chart.axes(Qt.Horizontal)[0].setGridLineVisible(True)

        # 将图表添加到QChartView中
        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.chart_view.setRubberBand(QChartView.HorizontalRubberBand)

        # 设置新view
        self.chart_view_2 = QChartView(self.chart_2)
        self.chart_view_2.setRenderHint(QPainter.Antialiasing)
        self.chart_view_2.setRubberBand(QChartView.HorizontalRubberBand)



        # 将QChartView添加到窗口中心区域
        v_layout = QVBoxLayout(central_widget)
        v_layout.addWidget(self.chart_view)
        v_layout.addWidget(self.chart_view)
        v_layout.addWidget(self.chart_view_2)
        self.setLayout(v_layout)


        # 添加控件
        # 创建下拉框1
        self.combo_box1 = QComboBox()
        self.combo_box1.addItems(['Line Chart 1', 'Line Chart 2'])
        # self.combo_box1.currentIndexChanged.connect(self.handle_combo_box1)

        # 创建下拉框2
        self.combo_box2 = QComboBox()
        self.combo_box2.addItems(['Line Chart 3', 'Line Chart 4'])
        # self.combo_box2.currentIndexChanged.connect(self.handle_combo_box2)

        # 创建按钮
        self.button = QPushButton('Start Training')
        # self.button.clicked.connect(self.start_training)

        # 添加下拉框1、下拉框2和按钮到窗口中
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.combo_box1)
        h_layout.addWidget(self.combo_box2)
        h_layout.addStretch()
        h_layout.addWidget(self.button)

        v_layout.addLayout(h_layout)
    def update_chart(self, epoch, loss, accuracy):
        # 在图表中添加新的点
        self.loss_series.append(epoch, loss)
        self.acc_series.append(epoch, accuracy)

        # 更新x轴范围
        if epoch >= self.chart.axisX().max():
            self.chart.axisX().setRange(0, epoch + 1)

        # 更新y轴范围
        if loss >= self.chart.axisY().max() or accuracy >= self.chart.axisY().max():
            max_value = max(loss, accuracy)
            self.chart.axisY().setRange(0, max_value + max_value * 0.1)

        # 重绘图表
        self.chart_view.update()

    def update_chart2(self, epoch, loss, accuracy):
        self.loss_series_2.append(epoch, loss)
        self.acc_series_2.append(epoch, accuracy)

        if epoch >= self.chart_2.axisX().max():
            self.chart_2.axisX().setRange(0, epoch + 1)

        if loss >= self.chart_2.axisY().max() or accuracy >= self.chart_2.axisY().max():
            max_value = max(loss, accuracy)
            self.chart_2.axisY().setRange(0, max_value + max_value * 0.1)

        self.chart_view_2.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 创建并显示主窗口
    my_window = MyWindow()
    my_window.show()

    # 模拟训练过程，每秒更新一次图表
    epoch = 0
    loss = 0.7
    accuracy = 0.5
    while True:
        my_window.update_chart(epoch, loss, accuracy)
        my_window.update_chart2(epoch,loss,accuracy)
        # 更新数据
        epoch += 1
        loss -= 0.02
        accuracy += 0.01

        # 如果更新到一定程度则停止
        if epoch == 30:
            break

        # 睡眠一秒钟以模拟实际训练过程
        QApplication.processEvents()
        QThread.sleep(1)

    sys.exit(app.exec_())