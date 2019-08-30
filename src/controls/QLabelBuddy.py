# -*- coding:utf-8 -*-

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette, QPixmap
from PyQt5.QtCore import Qt


class QLabelBuddy(QDialog):
    def __init__(self):
        super(QLabelBuddy, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QLabel与伙伴控件')

        nameLabel = QLabel('&Name', self)
        nameLineEdit = QLineEdit(self)
        nameLabel.setBuddy(nameLineEdit)

        passwordLabel = QLabel('&Password', self)
        passwordLineEdit = QLineEdit(self)
        passwordLabel.setBuddy(passwordLineEdit)

        btnOk = QPushButton('&OK')
        btnCancel = QPushButton('&Cancel')

        mainLayout = QGridLayout(self)
        mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addWidget(nameLineEdit, 0, 1, 1, 2)

        mainLayout.addWidget(passwordLabel, 1, 0)
        mainLayout.addWidget(passwordLineEdit,1, 1, 1, 2)

        mainLayout.addWidget(btnOk, 2, 1)
        mainLayout.addWidget(btnCancel, 2, 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelBuddy()
    main.show()
    sys.exit(app.exec_())