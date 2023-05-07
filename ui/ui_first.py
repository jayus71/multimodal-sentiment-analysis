# 测试pyqt5图形界面
# update-1：仅创建图形界面
# upated-2：添加信号，槽函数
# update-3：封装到类中
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox

# def handleCalc():
#     print('the button is clicked')

# app = QApplication([])

# window = QMainWindow()
# window.resize(600, 600)
# window.move(400, 400)
# window.setWindowTitle("test")

# textEdit = QPlainTextEdit(window)
# textEdit.setPlaceholderText("please input the salary info")
# textEdit.resize(300, 300)
# textEdit.move(10, 25)

# button = QPushButton('calc', window)
# button.move(350, 100)
# button.clicked.connect(handleCalc)

# window.show()
# app.exec_()

class stats:
    def __init__(self):
        self.window = QMainWindow()
        self.window.resize(600, 600)
        self.window.move(400, 100)
        self.window.setWindowTitle("test")

        self.textEdit = QPlainTextEdit(self.window)
        self.textEdit.setPlaceholderText('please input the salary info')
        self.textEdit.move(10, 25)
        self.textEdit.resize(300, 350)

        self.button = QPushButton('calc', self.window)
        self.button.move(380, 80)

        self.button.clicked.connect(self.handleCalc)


    def handleCalc(self):
        info = self.textEdit.toPlainText()

        # 薪资20000 以上 和 以下 的人员名单
        salary_above_20k = ''
        salary_below_20k = ''
        for line in info.splitlines():
            if not line.strip():
                continue
            parts = line.split(' ')
            # 去掉列表中的空字符串内容
            parts = [p for p in parts if p]
            name,salary,age = parts
            if int(salary) >= 20000:
                salary_above_20k += name + '\n'
            else:
                salary_below_20k += name + '\n'

        QMessageBox.about(self.window,
                    '统计结果',
                    f'''薪资20000 以上的有：\n{salary_above_20k}
                    \n薪资20000 以下的有：\n{salary_below_20k}'''
                    )

app = QApplication([])
stats = stats()
stats.window.show()
app.exec_()