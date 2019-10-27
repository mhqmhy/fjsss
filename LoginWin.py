import sys
import pygame
from PyQt5.QtWidgets import QApplication, QWidget,QLineEdit
from PyQt5.QtGui import QFont
from loginWinUi import Ui_Form
from linkServer import LoginAccount
import MainPage


class StartWin(Ui_Form,QWidget):

    def __init__(self):
        super(StartWin,self).__init__()
        self.setWindowTitle('登录界面')
        self.setupUi(self)
        self.win = MainPage.MainWindow()
        self.cl=LoginAccount()
        self.initUi()
    def initUi(self):
        self.login_passwd.setEchoMode(QLineEdit.Password)#密码框隐藏 PasswordEchoOnEdit Password
        self.login_userName.setText('SheepHuan')
        self.login_passwd.setText('GoodJob')
        self.login_userName.setFont(QFont('Cosolas',14))
        self.login_passwd.setFont(QFont('Cosolas', 14))
        self.SI_userName.setFont(QFont('Cosolas', 14))
        self.SI_passwd.setFont(QFont('Cosolas', 14))
        # self.SI_passwdAgain.setFont(QFont('Cosolas', 14))
        self.loginBtn.clicked.connect(self.login)
        self.signInBtn.clicked.connect(self.signIn)
    def login(self):
        # win.close()
        account = {
            "username": '',
            "password": ''
        }
        account["username"]=self.login_userName.text()
        account["password"]=self.login_passwd.text()
        if account["username"] and account["password"]:
            try:
                if self.cl.login(account)=='OK':
                    try:
                        self.win.getUserInfo(self.cl.check())
                        self.win.show()
                        self.close()
                    except Exception as e:
                        print(e)

            except Exception as e:
                print(e)


    def signIn(self):
        # win.close()
        account = {
            "username": '',
            "password": '',
            "student_number":'',
            "student_password":''
        }
        account["username"] = self.SI_userName.text()
        # if self.SI_passwd.text()==self.SI_passwdAgain.text():
        account["password"] = self.SI_passwd.text()
        account["student_number"]=self.SI_student_number
        account["student_password"]=self.SI_student_passwd
        print(account)
        if account["username"] and account["password"]:
            try:
                if self.cl.signIn(account)!='error':
                    self.win.getUserInfo(self.cl.check())
                    self.win.show()
                    self.hide()
                else:
                    print("注册失败")
            except:
                pass
        else:
            print('注册失败')


if __name__=="__main__":
    app = QApplication(sys.argv)
    demo = StartWin()
    demo.show()

    sys.exit(app.exec_())