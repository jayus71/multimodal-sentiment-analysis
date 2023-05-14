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
        self.setGeometry(100, 100, 800, 800)

        # 设置中心窗口，用于显示图形
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # 创建数据系列
        self.loss_series = QLineSeries()
        self.loss_series.setName('Train Loss')

        self.acc_series = QLineSeries()
        self.acc_series.setName('Train Accuracy')

        # 添加新区域
        self.loss_series_2 = QLineSeries()
        self.loss_series_2.setName('Val Loss')

        self.acc_series_2 = QLineSeries()
        self.acc_series_2.setName('Val Accuracy')

        self.chart_2 = QChart()
        self.chart_2.setTheme(QChart.ChartThemeLight)
        self.chart_2.setTitle('Val Loss and Accuracy Graph')

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
        self.chart.setTitle('Train Loss and Accuracy Graph')

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


        # # 添加控件
        # # 创建下拉框1
        # self.combo_box1 = QComboBox()
        # self.combo_box1.addItems(['Line Chart 1', 'Line Chart 2'])
        # # self.combo_box1.currentIndexChanged.connect(self.handle_combo_box1)

        # # 创建下拉框2
        # self.combo_box2 = QComboBox()
        # self.combo_box2.addItems(['Line Chart 3', 'Line Chart 4'])
        # # self.combo_box2.currentIndexChanged.connect(self.handle_combo_box2)

        # # 创建按钮
        # self.button = QPushButton('Start Training')
        # # self.button.clicked.connect(self.start_training)

        # # 添加下拉框1、下拉框2和按钮到窗口中
        # h_layout = QHBoxLayout()
        # h_layout.addWidget(self.combo_box1)
        # h_layout.addWidget(self.combo_box2)
        # h_layout.addStretch()
        # h_layout.addWidget(self.button)

        # v_layout.addLayout(h_layout)
    def update_chart(self, epoch, loss, accuracy):
        # 在图表中添加新的点
        self.loss_series.append(epoch, loss)
        self.acc_series.append(epoch, accuracy)

        # 更新x轴范围
        if epoch >= self.chart.axisX().max():
            self.chart.axisX().setRange(1, epoch)

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
            self.chart_2.axisX().setRange(1, epoch)

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
    epoch = 1
    loss = 1.2
    accuracy = 0.4
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