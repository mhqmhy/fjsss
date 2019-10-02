# 登录界面
import sys
import pygame
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QLabel, QLineEdit, QPushButton, \
    QGridLayout, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QMovie,QPixmap

#自定义库
import LoginUi
from loadSrc import LoadSrc
import SignInPage



class LoginPage(QWidget,LoginUi.Ui_Form):

    def __init__(self):
        super(LoginPage,self).__init__()

        #设置窗口大小
        self.setMinimumSize(600,523)
        self.setMaximumSize(600,523)
        self.setupUi(self)
        self.setWindowTitle('登录界面')
        #self.setWindowFlags(self.FramelessWindowHint) #设置窗口无边框
        self.initUi()
        self.LoginCartoon_init()
        self.signIn=SignInPage.SignIn()

    def initUi(self):#信号连接事件
        self.SignInBtn.clicked.connect(self.signInEvent)
        self.SignUpBtn.clicked.connect(self.signUpEvent)

    def signInEvent(self): #跳转到注册页面
        self.signIn.exec_()

    def signUpEvent(self): #检验账号密码正确性，跳转到主界面
        pass


    def LoginCartoon_init(self): #加载动画、音乐和默认头像
        #加载GIF的方法 https://www.jb51.net/article/163177.htm
        gif=QMovie(LoadSrc('./src/login_Cartoon.gif'))
        self.login_cartoon.setMovie(gif)
        self.loginAvtar_init()
        gif.start()
        self.loadBGM()

    def loginAvtar_init(self,path='./src/default_Avatar.jpg'):
        imgPath=LoadSrc(path)
        pix=QPixmap(imgPath)
        self.avatar.setPixmap(pix)

    def loadBGM(self,path='./src/login_BGM.mp3'): #加载bgm https://www.zhangshengrong.com/p/KWa3jYAz1o/
        pygame.mixer.init()
        bgmPath=LoadSrc(path)
        pygame.mixer.music.load(bgmPath)
        pygame.mixer.music.play(loops=-1) #相关设置 https://blog.csdn.net/qq_41556318/article/details/86305046




if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = LoginPage()
    demo.show()
    sys.exit(app.exec_())