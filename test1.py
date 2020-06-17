# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
import pymysql
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from pymysql import Connection
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(100, 100, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 150, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(250, 130, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.buttonClicked)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "PushButton"))

    def buttonClicked(self):
        sender = self.sender()

        mysql_conn()


def mysql_conn():
    # 连接数据库用
    conn = Connection(host='localhost', user='root', password='1234abcd', port=3306, database='db1')
    cursor = conn.cursor()
    # 往名为l的表格中插入姓名和对应年龄

    # 插入内容写好后要进行提交
    sttr="大学"
    # cursor.execute('drop table aa')
    cursor.execute("insert into tb1(name) values (sttr)")
    # 数据库事务的提交
    conn.commit()

    # 测试是否提交成功
    print('插入成功！')

    # 提取表中第一个内容
    # print(cursor.fetchone())
    # 如果提取过第一个内容，则是提取前三个
    # print(cursor.fetchmany(3))
    # 如运行过前两个，则显示除提取后剩下的全部
    # print(cursor.fetchall())

    # 结束关闭 cursor  connection
    cursor.close()
    conn.close()


class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()

    myWin.show()
    sys.exit(app.exec_())
