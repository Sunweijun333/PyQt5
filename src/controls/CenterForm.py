# QDesktopWidget
# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QDesktopWidget, QMainWindow, QApplication
# from PyQt5.QtGui import QIcon


class CenterForm(QMainWindow):
    def __init__(self, parent=None):
        super(CenterForm, self).__init__(parent)

        self.setWindowTitle('主窗口居中')
        self.resize(400, 300)
        self.center()

    def center(self):
        # 屏幕坐标
        screen = QDesktopWidget().screenGeometry()
        # 窗口坐标
        size = self.geometry()
        newLeft = (screen.width() - size.width())/2
        newTop = (screen.height() - size.height())/2
        self.move(newLeft, newTop)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon('./images/icon.ico'))
    main = CenterForm()
    # main.center()
    main.show()
    sys.exit(app.exec_())

