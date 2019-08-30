# QDesktopWidget
# -*- coding:utf-8 -*-

import sys

from PyQt5.QtWidgets import QDesktopWidget, QMainWindow, QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPalette, QPixmap
from PyQt5.QtCore import Qt

'''
    QLabel 常用的信号（事件）
    1. 当鼠标划过QLabel触发        linkHoverd
    2. 单击QLabel                 linkActivated
'''


class QLabelDemo(QWidget):
    def __init__(self):
        super(QLabelDemo, self).__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)
        label1.setText("<font color=yellow>这是一个文本标签.</font>")
        label1.setAutoFillBackground(True)
        palette = QPalette()
        # 设置背景颜色
        palette.setColor(QPalette.Window, Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)
        label2.setText("<a href='#'>欢迎使用Python GUI程序</a>")
        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('这是一个图片')
        label3.setPixmap(QPixmap("./images/predictions.jpg"))

        # 让链接生效
        label4.setOpenExternalLinks(True)
        label4.setText("<a href ='http://www.baidu.com'>点击访问百度</a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('这时一个超级链接')

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        label2.linkHovered.connect(self.link_hoverd)
        label4.linkActivated.connect(self.link_clicked)
        self.setLayout(vbox)
        self.setWindowTitle("QLabel控件演示")

    def link_hoverd(self):
        print "当鼠标划过label2触发"

    def link_clicked(self):
        print "当鼠标划过label4触发"


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelDemo()
    main.show()
    sys.exit(app.exec_())