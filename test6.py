import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5 import QtWidgets
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    windows=QtWidgets.QMainWindow()

    windows.setWindowTitle("dd")
    windows.resize(600,600)
    win=QtWidgets.QWidget(windows)

    win.resize(600,600)
    button=QtWidgets.QPushButton(win)
    #button.setGeometry(QtCore.QRect(180, 360, 54, 12))


    button.move(300,200)
    button.setText("打开")
    windows.show()
    sys.exit(app.exec())
