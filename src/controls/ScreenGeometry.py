# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QApplication, QPushButton, QWidget


def onclick_button():
    print "1"
    print "widget.x() = ", widget.x()
    print "widget.y() = ", widget.y()
    print "widget.width() = ", widget.width()
    print "widget.height() = ", widget.height()
    print "2:不包含标题栏"
    print "widget.geometry().x() = ", widget.geometry().x()
    print "widget.geometry().y() = ", widget.geometry().y()
    print "widget.geometry().width() = ", widget.geometry().width()
    print "widget.geometry().height() = ", widget.geometry().height()
    print "3:高度包含标题栏"
    print "widget.frameGeometry().x() = ", widget.frameGeometry().x()
    print "widget.frameGeometry().y() = ", widget.frameGeometry().y()
    print "widget.frameGeometry().width() = ", widget.frameGeometry().width()
    print "widget.frameGeometry().height() = ", widget.frameGeometry().height()


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

