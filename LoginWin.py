import sys
import pygame
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QPushButton,QVBoxLayout,QHBoxLayout
from PyQt5.QtGui import QMovie,QPixmap,QCursor,QPalette,QBrush,QIcon
from PyQt5.QtCore import Qt
from loginWinUi import Ui_Form
from linkServer import LoginAccount

class StartWin(Ui_Form,QWidget):

    def __init__(self):
        super(StartWin,self).__init__()
        self.setWindowTitle('登录界面')
        self.setupUi(self)
        self.tabWidget.setAttribute(Qt.WA_TranslucentBackground)
        self.cl=LoginAccount()
        self.initUi()
    def initUi(self):
        self.loginBtn.clicked.connect(self.login)
        self.signInBtn.clicked.connect(self.signIn)
    def login(self):
        account = {
            "username": '',
            "password": ''
        }
        account["username"]=self.login_userName.text()
        account["password"]=self.login_passwd.text()
        if account["username"] and account["password"]:
            try:
                self.cl.login(account)
            except:
                pass


    def signIn(self):
        account = {
            "username": '',
            "password": ''
        }
        account["username"] = self.SI_userName.text()
        if self.SI_passwd.text()==self.SI_passwdAgain.text():
            account["password"] = self.SI_passwd.text()
            print(account)
            if account["username"] and account["password"]:
                try:
                    self.cl.signIn(account)
                except:
                    pass
        else:
            print('两次密码不一致')

if __name__=="__main__":
    app = QApplication(sys.argv)
    demo = StartWin()
    demo.show()
    sys.exit(app.exec_())