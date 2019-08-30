# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon


class FirstMainWin(QMainWindow):
    def __init__(self, parent=None):
        super(FirstMainWin,self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 260, 260)
        # 这种方式只能在windows下显示图标
        self.setWindowTitle('设置窗口图标')
        self.setWindowIcon(QIcon('./images/icon.ico'))
        self.status = self.statusBar()
        self.status.showMessage('只存在5s的消息', 5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 设置应用程序图标
    # app.setWindowIcon(QIcon('./images/icon.ico'))
    main = FirstMainWin()
    main.show()
    sys.exit(app.exec_())

