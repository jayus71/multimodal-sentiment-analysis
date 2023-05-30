import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, QLabel, QTextEdit
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QUrl


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("情感分析")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.video_widget = QVideoWidget()
        self.video_widget.setMinimumSize(600, 400)  # 调整视频播放区域的大小
        self.layout.addWidget(self.video_widget)

        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.video_widget)

        self.file_button = QPushButton("选择mp4文件")
        self.file_button.clicked.connect(self.select_file)

        self.video_layout = QHBoxLayout()
        self.video_layout.addWidget(self.file_button)
        self.layout.addLayout(self.video_layout)

        self.analyze_button = QPushButton("点击分析")
        # self.analyze_button.clicked.connect(self.analyze)
        self.layout.addWidget(self.analyze_button)

        self.single_label = QLabel("单模态结果：")
        self.layout.addWidget(self.single_label)

        self.single_result_text_edit = QTextEdit()
        self.layout.addWidget(self.single_result_text_edit)
        self.single_result_text_edit.setText("文本：开心\n语音：兴奋\n图像：开心\n")

        self.multi_label = QLabel("多模态结果：")
        self.layout.addWidget(self.multi_label)

        self.multi_result_text_edit = QTextEdit()
        self.layout.addWidget(self.multi_result_text_edit)
        self.multi_result_text_edit.setText("多模态结果：开心")

    def select_file(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("MP4 files (*.mp4)")
        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
            self.player.play()

            # self.single_result_text_edit.clear()
            # self.multi_result_text_edit.clear()
            self.single_label.setText(f"单模态结果：（选择的文件：{file_path}）")
            self.multi_label.setText(f"多模态结果：（选择的文件：{file_path}）")

    # def analyze(self):
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
