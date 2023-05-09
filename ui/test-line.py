import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QVBoxLayout, QPushButton,QWidget
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QValueAxis
from PyQt5.QtCore import Qt, QPointF
from PyQt5 import QtGui 



class LossAccuracyPlot(QMainWindow):
    def __init__(self, loss_data, accuracy_data):
        super().__init__()

        self.loss_data = loss_data
        self.accuracy_data = accuracy_data

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Loss and Accuracy Plot')

        main_layout = QVBoxLayout()

        self.chart_view = self.create_chart_view()

        update_button = QPushButton("Update Data")
        update_button.clicked.connect(self.update_data)

        main_layout.addWidget(self.chart_view)
        main_layout.addWidget(update_button)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)

        self.setCentralWidget(central_widget)
        self.resize(800, 600)

    def create_chart_view(self):
        series_loss = QLineSeries()
        series_accuracy = QLineSeries()

        chart = self.create_chart(series_loss, series_accuracy)

        chart_view = QChartView(chart)
        chart_view.setRenderHint(QtGui.QPainter.Antialiasing)

        return chart_view

    def create_chart(self, series_loss, series_accuracy):
        for i, (loss, accuracy) in enumerate(zip(self.loss_data, self.accuracy_data), start=1):
            series_loss.append(QPointF(i, loss))
            series_accuracy.append(QPointF(i, accuracy))

        chart = QChart()
        chart.addSeries(series_loss)
        chart.addSeries(series_accuracy)

        chart.setTitle('Loss and Accuracy Plot')
        chart.createDefaultAxes()

        chart.legend().setAlignment(Qt.AlignBottom)
        series_loss.setName('Loss')
        series_accuracy.setName('Accuracy')

        return chart

    def update_data(self):
        # 模拟更新数据
        self.loss_data.append(self.loss_data[-1] - 0.1)
        self.accuracy_data.append(self.accuracy_data[-1] + 0.1)

        # 删除旧的折线图
        old_chart_view = self.chart_view
        self.chart_view = self.create_chart_view()
        old_chart_view.deleteLater()

        # 更新界面上的折线图
        layout = self.centralWidget().layout()
        layout.insertWidget(0, self.chart_view)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 示例数据
    loss_data = [1, 0.8, 0.6, 0.4, 0.2]
    accuracy_data = [0.5, 0.6, 0.7, 0.8, 0.85]

    main_window = LossAccuracyPlot(loss_data, accuracy_data)
    main_window.show()

    sys.exit(app.exec_())