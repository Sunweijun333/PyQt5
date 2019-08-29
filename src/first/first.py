# -*- coding: UTF-8 -*-
import sys
from PyQt5.QtWidgets import QApplication,QWidget

if __name__ == '__main__':
    # 创建QApplication类的实例
    app = QApplication(sys.argv)
    # 创建一个窗口
    w = QWidget()
    w.resize(500, 200)
    w.move(300, 400)

    w.setWindowTitle('第一个基于PyQt5的桌面应用')
    w.show()

    sys.exit(app.exec_())