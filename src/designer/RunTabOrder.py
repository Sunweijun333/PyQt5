import sys
import TabOrder

from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWin = QMainWindow()
    ui = TabOrder.Ui_MainWindow()
    ui.setupUi(MainWin)
    MainWin.show()
    sys.exit(app.exec_())
