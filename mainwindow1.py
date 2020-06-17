import sys
from PyQt5 import QtWidgets
from mainwindow import Ui_MainWindow

class MyPyQT_Form(QtWidgets.QWidget,Ui_MainWindow):
    def __init__(self):
        super(MyPyQT_Form,self).__init__()
        self.setupUi(self)

    #实现pushButton_click()函数，textEdit是我们放上去的文本框的id
    def pushButton_click(self):
        print("ddddddd")
        #self.textEdit.setText("你点击了按钮")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.show()
    sys.exit(app.exec_())