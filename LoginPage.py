# 登录界面
import sys
import pygame
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QPushButton,QVBoxLayout,QHBoxLayout
from PyQt5.QtGui import QMovie,QPixmap,QCursor,QPalette,QBrush,QIcon
from PyQt5.QtCore import Qt
#自定义库
import LoginUi
from loadSrc import LoadSrc
from MainPage import MainWindow
import SignInPage


class LoginPage(QWidget,LoginUi.Ui_Form):

    def __init__(self):
        super(LoginPage,self).__init__()
        self.setCursor(QCursor(QPixmap('./src/mouse40.png')))
        #设置窗口大小
        self.setMinimumSize(720,487)
        self.setMaximumSize(720,487)
        #设置背景图片
        palette=QPalette()
        palette.setBrush(self.backgroundRole(),QBrush(QPixmap('./src/背景2.jpg')))
        self.setPalette(palette)
        self.setupUi(self)
        self.setWindowTitle('登录界面')
        self.loadBGM()
        #self.setWindowFlags(self.FramelessWindowHint) #设置窗口无边框
        self.initUi()
        # self.LoginCartoon_init()
        # self.signIn=SignInPage.SignIn()

    def initUi(self):#信号连接事件

        self.qqBtn=QPushButton(self)
        self.qqBtn.setStyleSheet("QPushButton{border-image: url(./src/icon/login_btn_qq.png)}")
        self.wxBtn=QPushButton(self)
        self.wxBtn.setStyleSheet("QPushButton{border-image: url(./src/icon/login_btn_wx.png)}")
        self.zhBtn = QPushButton(self)
        self.zhBtn.setStyleSheet("QPushButton{border-image: url(./src/icon/login_btn_zh.png)}")
        self.qqBtn.setGeometry(10,10,100,35)
        self.wxBtn.setGeometry(120,10,100,35)
        self.zhBtn.setGeometry(230,10,100,35)
        # self.SignInBtn.clicked.connect(self.signInEvent)
        self.zhBtn.clicked.connect(self.signUpEvent)

    def signInEvent(self): #跳转到注册页面
        pass
        # self.signIn.exec_()

    def signUpEvent(self): #检验账号密码正确性，跳转到主界面
        #直接校验正确
        win.show()
        self.close()


    def loadBGM(self,path=r'.\src\bgm\MusicEx\MusicEx_Welcome.ogg'): #加载bgm https://www.zhangshengrong.com/p/KWa3jYAz1o/
        pygame.mixer.init()
        bgmPath=LoadSrc(path)
        pygame.mixer.music.load(bgmPath)
        pygame.mixer.music.play(loops=-1) #相关设置 https://blog.csdn.net/qq_41556318/article/details/86305046



if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = LoginPage()
    demo.show()
    win = MainWindow()
    sys.exit(app.exec_())