import sys
from MainPageUi import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QLabel,QPushButton
from PyQt5.QtGui import QMovie,QPixmap,QCursor,QPalette,QBrush,QFont,QIcon
from PyQt5 import QtCore


class Room(QWidget):
    def __init__(self):
        super(QWidget,self).__init__()
        self.setWindowTitle('游戏界面')
        self.setObjectName('GameWindow')
        self.setMinimumSize(1200, 811)
        self.setMaximumSize(1200, 811)
        # self.setStyleSheet("#MainWindow{border-image:url(./src/room_bc1.png);}")
        self.loadBg()
        self.loadTable()
        self.start()
        self.initUi()
    def initUi(self):
        self.startBtn.clicked.connect(self.closeStartBtn)

    def loadBg(self):
        self.setCursor(QCursor(QPixmap('./src/mouse40.png')))
        palette = QPalette()
        palette.setBrush(self.backgroundRole(), QBrush(QPixmap('./src/room_bc1.png')))
        self.setPalette(palette)
    def loadTable(self):
        table = QLabel(self)
        table.setPixmap(QPixmap('./src/桌子.png'))
        table.setGeometry(150, 410, 900, 700)
        table.setScaledContents(True)  # 让图片自适应label大小

    def loadPai(self):
        pass

    def start(self):
        self.startBtn=QPushButton(self)
        self.startBtn.setStyleSheet("QPushButton{border-image: url(./src/开始游戏.png)}")
        self.startBtn.setGeometry(540,400,125,60)

    def closeStartBtn(self):
        self.startBtn.close()
        #开始发牌!!!
    def startGame(self):
        pass

    def startDeal(self): #发牌
        

if __name__=="__main__":
    app = QApplication(sys.argv)
    demo = Room()
    demo.show()
    sys.exit(app.exec_())