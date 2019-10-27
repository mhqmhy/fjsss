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
        try:
            self.initData()
            self.initUi()
            self.hall=None
        except Exception as e:
            print(e)


    def initUi(self):
        #注意控制加载图片的顺序
        #加载房间背景
        self.setCursor(QCursor(QPixmap('./src/mouse40.png')))
        palette = QPalette()
        palette.setBrush(self.backgroundRole(), QBrush(QPixmap('./src/room_bc1.png')))
        self.setPalette(palette)
        #加载桌子的图片
        table = QLabel(self)
        table.setPixmap(QPixmap('./src/桌子.png'))
        table.setGeometry(150, 410, 900, 700)
        table.setScaledContents(True)  # 让图片自适应label大小
        # 加载头像
        headFrame = QLabel(self)  # 加载头像边框
        headFrame.setPixmap(QPixmap('./src/headTopFrame.png'))
        headFrame.setGeometry(295, 700, 100, 100)
        headFrame.setScaledContents(True)  # 让图片自适应label大小
        avatar = QLabel(self)  # 加载头像图片,默认男性头像
        avatar.setPixmap(QPixmap('./src/headBoy.png'))
        avatar.setGeometry(300, 705, 90, 90)
        avatar.setScaledContents(True)  # 让图片自适应label大小
        #加载扑克牌位置
        self.showMyPai()
        #加载三个按钮 再来一局、开始游戏和离开游戏三个
        self.gameAgain=QPushButton(self)
        self.gameAgain.setStyleSheet("QPushButton{border-image: url(./src/再来一局.png)}")
        self.gameAgain.setGeometry(800, 10, 125, 50)
        self.startBtn = QPushButton(self)
        self.startBtn.setStyleSheet("QPushButton{border-image: url(./src/开始游戏.png)}")
        self.startBtn.setGeometry(540, 400, 125, 60)
        self.quitBtn = QPushButton(self)
        self.quitBtn.setStyleSheet("QPushButton{border-image: url(./src/top_btn_exit.png)}")
        self.quitBtn.setGeometry(0, 8, 60, 62)

        self.startBtn.clicked.connect(self.startGame)
        self.quitBtn.clicked.connect(self.quitRoom)
        self.gameAgain.clicked.connect(self.startGame)

    def initData(self):
        self.mypokes=[]
        self.server=linkServer.Game()

    def getUserInfo(self,userInfo):
        try:
            self.userInfo = userInfo
        except Exception as e:
            print(e)


    def showMyPai(self):
        self.pokes=[]
        for i in range(13):
            x = QPushButton(self)
            x.setStyleSheet("QPushButton{border-image: url(./src/cardBack.png)}")
            x.setGeometry(450+22*i, 680, 73, 100)
            self.pokes.append(x)

    def quitRoom(self):
        self.close()

    def startGame(self):
        try:
            self.startBtn.close()
            print(self.userInfo["token"])
            self.mypokes=self.server.openGame(self.userInfo["token"])
            #开始发牌!!!
            print("token",self.mypokes)
            #将牌传入出牌算法

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
                #出牌
            card=[]
            one=self.mypokes[0]+' '+self.mypokes[1]+' '+self.mypokes[2]
            two=self.mypokes[3]+' '+self.mypokes[4]+' '+self.mypokes[5]+' '+self.mypokes[6]+' '+self.mypokes[7]
            three=self.mypokes[8]+' '+self.mypokes[9]+' '+self.mypokes[10]+' '+self.mypokes[11]+' '+self.mypokes[12]
            card.append(one)
            card.append(two)
            card.append(three)
            print(card)
            self.server.submitPoke(self.userInfo["token"],card)
        except Exception as e:
            print('Game/startgame',e)


if __name__=="__main__":
    app = QApplication(sys.argv)
    demo = Room()
    demo.show()
    sys.exit(app.exec_())