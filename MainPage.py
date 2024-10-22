import sys
from MainPageUi import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QLabel,QPushButton
from PyQt5.QtGui import QMovie,QPixmap,QCursor,QPalette,QBrush,QFont,QIcon
from PyQt5 import QtCore
from Game import Room
#QMainWindow,Ui_MainWindow,
import history
import ranking
class MainWindow(QWidget): #绝对定位布局

    def __init__(self):
        super(MainWindow,self).__init__()
        self.setWindowTitle("登录界面")
        #self.setMinimumSize(1680, 1136)
        self.setMinimumSize(1000, 676)
        # self.setMaximumSize(1000, 1006)
        self.setMaximumSize(1000, 676)

        palette = QPalette()
        palette.setBrush(self.backgroundRole(), QBrush(QPixmap('./src/TableBG/room_bj_laizi_1_kp.jpg')))
        self.setPalette(palette)
        self.setCursor(QCursor(QPixmap('./src/mouse40.png')))
        self.initUi()
    def getUserInfo(self,dict):
        self.userInfo=dict
        self.account=dict["account"]
        self.token=dict["token"]
        self.user_id=dict["user_id"]

    def initUi(self):
        #加载头像
        headFrame = QLabel(self)
        headFrame.setPixmap(QPixmap('./src/headTopFrame.png'))
        headFrame.setGeometry(2, 2, 100, 100)
        headFrame.setScaledContents(True)  # 让图片自适应label大小
        avatar = QLabel(self)
        avatar.setPixmap(QPixmap('./src/headBoy.png'))
        avatar.setGeometry(7, 7, 90, 90)
        avatar.setScaledContents(True)  # 让图片自适应label大小
        #加载姓名
        name = QLabel(self)
        name.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        name.setText("往事随风")
        name.setGeometry(90, 10, 100, 25)
        name.setFont(QFont("Microsoft YaHei"))
        name.setStyleSheet("QLabel{color:rgb(255,250,250,255);font-size:20px;font-weight:bold;}")
        self.rankingListBtn=QPushButton(self)
        self.historyListBtn=QPushButton(self)
        self.rankingListBtn.setStyleSheet("QPushButton{border-image: url(./src/排行榜.png)}")
        self.historyListBtn.setStyleSheet("QPushButton{border-image: url(./src/历史记录.png)}")
        self.rankingListBtn.setGeometry(5,120, 100,40)
        self.historyListBtn.setGeometry(5,170,100,40)
        settingBtn=QPushButton(self)
        settingBtn.setStyleSheet("QPushButton{border-image: url(./src/top_btn_settings.png)}")
        settingBtn.setGeometry(890,10,60,60)

        self.init_RoomLevel()
        self.level1.clicked.connect(self.jump2Level1)
        self.historyListBtn.clicked.connect(self.jump2History)
        self.rankingListBtn.clicked.connect(self.jump2Ranking)
    def jump2History(self):
        self.hisWin=history.History()
        self.hisWin.show()

    def jump2Ranking(self):
        self.rankWin=ranking.RankList()
        self.rankWin.show()

    def jump2Level1(self):
        print(self.userInfo)
        try:
            self.onegame = Room( )
            self.onegame.getUserInfo(self.userInfo)
            self.onegame.show()
        except Exception as e:
            print('MainPage/jump2Level1()',e)
    def jump2Level2(self):
        pass

    def jump2Level3(self):
        pass

    def jump2Level4(self):
        pass
    def init_RoomLevel(self):
        frame1 = QLabel(self)
        frame1.setPixmap(QPixmap('./src/room_bg_level1.png'))
        frame1.setGeometry(150, 200, 170, 225)
        frame1.setScaledContents(True)
        self.level1 = QPushButton(self)
        self.level1.setStyleSheet("QPushButton{border-image: url(./src/room_frame.png)}")
        self.level1.setGeometry(150, 200, 170, 225)

        frame2 = QLabel(self)
        frame2.setPixmap(QPixmap('./src/room_frame.png'))
        frame2.setGeometry(340, 200, 170, 225)
        frame2.setScaledContents(True)
        self.level2 = QPushButton(self)
        self.level2.setStyleSheet("QPushButton{border-image: url(./src/room_bg_level2.png)}")
        self.level2.setGeometry(340, 200, 170, 225)

        frame3 = QLabel(self)
        frame3.setPixmap(QPixmap('./src/room_frame.png'))
        frame3.setGeometry(530, 200, 170, 225)
        frame3.setScaledContents(True)
        self.level3 = QPushButton(self)
        self.level3.setStyleSheet("QPushButton{border-image: url(./src/room_bg_level3.png)}")
        self.level3.setGeometry(530, 200, 170, 225)

        frame4 = QLabel(self)
        frame4.setPixmap(QPixmap('./src/room_frame.png'))
        frame4.setGeometry(720, 200, 170, 225)
        frame4.setScaledContents(True)
        self.level4 = QPushButton(self)
        self.level4.setStyleSheet("QPushButton{border-image: url(./src/room_bg_level4.png)}")
        self.level4.setGeometry(720, 200, 170, 225)


if __name__=="__main__":
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()
    sys.exit(app.exec_())