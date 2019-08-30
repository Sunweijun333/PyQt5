# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QApplication, QPushButton, QWidget


def onclick_button():
    print "1"
    print "widget.x() = ", widget.x()    # 250 (窗口横坐标)
    print "widget.y() = ", widget.y()    # 200 (窗口纵坐标)
    print "widget.width() = ", widget.width()    # 300 (工作区宽度)
    print "widget.height() = ", widget.height()  # 240 (工作区高度)
    print "2:不包含标题栏"
    print "widget.geometry().x() = ", widget.geometry().x()    # 250 (工作区横坐标)
    print "widget.geometry().y() = ", widget.geometry().y()    # 228 (工作区纵坐标)
    print "widget.geometry().width() = ", widget.geometry().width()     # 300 (工作区宽度)
    print "widget.geometry().height() = ", widget.geometry().height()   # 240 (工作区高度)
    print "3:高度包含标题栏"
    print "widget.frameGeometry().x() = ", widget.frameGeometry().x()   # 250 (窗口横坐标)
    print "widget.frameGeometry().y() = ", widget.frameGeometry().y()   # 200 (窗口纵坐标)
    print "widget.frameGeometry().width() = ", widget.frameGeometry().width()   # 300 (窗口宽度)
    print "widget.frameGeometry().height() = ", widget.frameGeometry().height() # 268 (窗口高度)


app = QApplication(sys.argv)
widget = QWidget()
btn = QPushButton(widget)
btn.setText("按钮")
btn.clicked.connect(onclick_button)
btn.move(24, 52)
widget.resize(300, 240)   # 设置工作区的尺寸
widget.move(250, 200)
widget.setWindowTitle("屏幕坐标系")
widget.show()
sys.exit(app.exec_())

