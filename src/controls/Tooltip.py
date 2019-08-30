# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QApplication, QPushButton, QWidget, QToolTip
from PyQt5.QtGui import QFont


class TooltipForm(QMainWindow):
    def __init__(self):
        super(TooltipForm, self).__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SanSerif', 12))
        self.setToolTip('今天是<b>星期五</b>')
        self.setGeometry(300, 300, 200, 300)
        self.setWindowTitle('设置控件显示消息')
        # 添加button
        self.button1 = QPushButton('我的按钮')
        self.button1.setToolTip('这是一个按钮！')
        layout = QHBoxLayout()
        layout.addWidget(self.button1)
        mainframe = QWidget()
        mainframe.setLayout(layout)
        self.setCentralWidget(mainframe)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TooltipForm()
    main.show()
    sys.exit(app.exec_())