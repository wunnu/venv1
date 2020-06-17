#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/23 下午1:43
# @Author  : Aries
# @Site    :
# @File    : 1023-01-Event sender.py
# @Software: PyCharm


import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication,QLineEdit
from PyQt5.QtGui import QIntValidator
class Exp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        btn1 = QPushButton('加',self)
        btn1.move(30,50)

        btn2 = QPushButton('减',self)
        btn2.move(150,50)

        pIntvalidator = QIntValidator(self)
        pIntvalidator.setRange(1, 999999)

        self.linedit=QLineEdit("",self)
        self.linedit.move(2,3)
        self.linedit.setValidator(pIntvalidator)


        self.linedit1 = QLineEdit("", self)
        self.linedit1.move(2, 100)
        self.linedit1.setValidator(pIntvalidator)


        self.linedit2=QLineEdit("",self)
        self.linedit2.move(150,100)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked1)

        self.statusBar()

        self.setGeometry(300,300,290,150)
        self.setWindowFilePath('Event sender')
        self.show()
    def buttonClicked(self):
        sender = self.sender()
        int1=int(self.linedit.text())+int(self.linedit1.text())
        str1=str(int1)
        self.linedit2.setText(str1)
        self.statusBar().showMessage(str1)


    def buttonClicked1(self):
        sender = self.sender()
        str = self.linedit1.text()

        self.statusBar().showMessage(str)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Exp()

    sys.exit(app.exec_())
