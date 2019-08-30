# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QApplication, QPushButton, QWidget


class QuitApp(QMainWindow):
    def __init__(self):
        super(QuitApp, self).__init__()
        self.resize(300, 120)
        self.setWindowTitle('退出应用程序')

        # 添加button
        self.button1 = QPushButton('退出应用程序')
        self.button1.clicked.connect(self.onclick_button)
        layout = QHBoxLayout()
        layout.addWidget(self.button1)
        mainframe = QWidget()
        mainframe.setLayout(layout)
        self.setCentralWidget(mainframe)
    # 按钮单击事件的方法

    def onclick_button(self):
        sender = self.sender()
        print(sender.text())
        app = QApplication.instance()
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QuitApp()
    main.show()
    sys.exit(app.exec_())
