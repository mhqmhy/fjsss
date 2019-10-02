from SignInPageUi import Ui_Dialog
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QLabel, QLineEdit, QPushButton, \
    QGridLayout, QVBoxLayout, QHBoxLayout, QMessageBox


class SignIn(QDialog,Ui_Dialog):

    def __init__(self):
        super(SignIn,self).__init__()

        self.setupUi(self)
        self.setWindowTitle('注册界面')
        #self.setupUi(self)
        #self.setObjectName("Dialog")
        # QDialog固定界面大小
        self.setFixedSize(370, 356)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo=SignIn()
    #demo.setupUi(demo)
    demo.show()
    sys.exit(app.exec_())