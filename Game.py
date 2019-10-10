import sys
from MainPageUi import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QLabel,QPushButton
from PyQt5.QtGui import QMovie,QPixmap,QCursor,QPalette,QBrush,QFont,QIcon
from PyQt5 import QtCore
import linkServer

POKE_SIZE=(50,68)

class Room(QWidget):
    def __init__(self):
        super(QWidget,self).__init__()
        self.setWindowTitle('游戏界面')
        # self.setObjectName('GameWindow')
        self.setMinimumSize(1200, 811)
        self.setMaximumSize(1200, 811)
        # self.setStyleSheet("#MainWindow{border-image:url(./src/room_bc1.png);}")
        self.loadBg()
        try:
            self.initData()
            self.loadTable()
            self.initUi()
            self.showAvatar()
            self.showOthersAvatar()
            self.hall=None
        except Exception as e:
            print(e)


    def initUi(self):
        self.gameAgain=QPushButton(self)
        self.gameAgain.setStyleSheet("QPushButton{border-image: url(./src/再来一局.png)}")
        self.gameAgain.setGeometry(800, 10, 191, 74)
        self.startBtn = QPushButton(self)
        self.startBtn.setStyleSheet("QPushButton{border-image: url(./src/开始游戏.png)}")
        self.startBtn.setGeometry(540, 400, 125, 60)
        self.quitBtn = QPushButton(self)
        self.quitBtn.setStyleSheet("QPushButton{border-image: url(./src/top_btn_exit.png)}")
        self.quitBtn.setGeometry(0, 8, 60, 62)
        self.startBtn.clicked.connect(self.startGame)
        self.quitBtn.clicked.connect(self.quit)
        self.gameAgain.clicked.connect(self.startGame)

    def initData(self):
        self.mypokes=[]
        self.server=linkServer.Game()

    def getUserInfo(self,userInfo):
        try:
            self.userInfo = userInfo
        except Exception as e:
            print(e)

    def quit(self):
        if self.hall!=None:
            self.hall.show()
        self.close()

    def loadBg(self):
        self.setCursor(QCursor(QPixmap('./src/mouse40.png')))
        palette = QPalette()
        palette.setBrush(self.backgroundRole(), QBrush(QPixmap('./src/room_bc1.png')))
        self.setPalette(palette)
    def showAvatar(self):
        #展示自己的头像
        avatar1 = QLabel(self)
        avatar1.setPixmap(QPixmap('./src/headTopFrame.png'))
        avatar1.setGeometry(295, 700, 100, 100)
        avatar1.setScaledContents(True)  # 让图片自适应label大小
        avatar2 = QLabel(self)
        avatar2.setPixmap(QPixmap('./src/headBoy.png'))
        avatar2.setGeometry(300, 705, 90, 90)
        avatar2.setScaledContents(True)  # 让图片自适应label大小
    def showOthersAvatar(self):
        avatar1 = QLabel(self)
        avatar1.setPixmap(QPixmap('./src/headTopFrame.png'))
        avatar1.setGeometry(280, 550, 100, 100)
        avatar1.setScaledContents(True)  # 让图片自适应label大小
        avatar2 = QLabel(self)
        avatar2.setPixmap(QPixmap('./src/headBoy.png'))
        avatar2.setGeometry(285, 555, 90, 90)
        avatar2.setScaledContents(True)  # 让图片自适应label大小
    def loadTable(self):
        table = QLabel(self)
        table.setPixmap(QPixmap('./src/桌子.png'))
        table.setGeometry(150, 410, 900, 700)
        table.setScaledContents(True)  # 让图片自适应label大小

        self.showMyPai()
        self.showOthersPai()
    def showOthersPai(self):
        x = QPushButton(self)
        x.setStyleSheet("QPushButton{border-image: url(./src/cardBack.png)}")
        x.setGeometry(180, 550, 73, 100)
        y = QPushButton(self)
        y.setStyleSheet("QPushButton{border-image: url(./src/cardBack.png)}")
        y.setGeometry(950, 550 , 73, 100)
        z = QPushButton(self)
        z.setStyleSheet("QPushButton{border-image: url(./src/cardBack.png)}")
        z.setGeometry(500, 450, 73, 100)

    def showMyPai(self):
        self.pokes=[]
        for i in range(13):
            x = QPushButton(self)
            x.setStyleSheet("QPushButton{border-image: url(./src/cardBack.png)}")
            x.setGeometry(450+22*i, 680, 73, 100)
            self.pokes.append(x)

    def startGame(self):
        try:
            self.startBtn.close()
            print(self.userInfo["token"])
            self.mypokes=self.server.openGame(self.userInfo["token"])
            #开始发牌!!!
            print("token",self.mypokes)
            for y in self.pokes:
                x=self.mypokes[self.pokes.index(y)]
                if '$' in x:
                    index=13*3
                elif '&' in x:
                    index=13*2
                elif '*' in x:
                    index=13*1
                else:
                    index=0
                if 'A' in x:
                    index+=1
                elif 'K' in x:
                    index+=13
                elif 'Q' in x:
                    index+=12
                elif 'J' in x:
                    index+=11
                else:
                    index+=int(x[1:])
                try:
                    # print(index)
                    url='./src/pokes/Images_Cards_Card_1_'+str(index)+'.png'
                    y.setStyleSheet("QPushButton{border-image: url("+url+")}")
                except Exception as e:
                    print(e)
        except Exception as e:
            print('Game/startgame',e)


if __name__=="__main__":
    app = QApplication(sys.argv)
    demo = Room()
    demo.show()
    sys.exit(app.exec_())