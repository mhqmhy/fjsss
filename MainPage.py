import sys
from MainPageUi import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QLabel,QPushButton
from PyQt5.QtGui import QMovie,QPixmap,QCursor,QPalette,QBrush,QFont
from PyQt5 import QtCore
#QMainWindow,Ui_MainWindow,
class MainWindow(QWidget): #绝对定位布局

    def __init__(self):
        super(MainWindow,self).__init__()
        self.setObjectName('MainWindow')
        self.initUi()
        #self.setupUi(self)
        #self.setMinimumSize(1680, 1136)
        self.setMinimumSize(1000, 676)
        # self.setMaximumSize(1000, 1006)
        self.setMaximumSize(1000, 676)

        # self.setStyleSheet("#MainWindow{border-image:url(./src/hall1000.jpg);}")
        palette = QPalette()
        palette.setBrush(self.backgroundRole(), QBrush(QPixmap('./src/hall1000.jpg')))
        self.setPalette(palette)
        self.setCursor(QCursor(QPixmap('./src/mouse40.png')))


    def initUi(self):
        wlayout = QtWidgets.QVBoxLayout()  # 全局布局（1个）：水平
        hlayout = QtWidgets.QHBoxLayout()
        self.avatar_init()
        self.userName_init()
        self.room_init()
        self.topTab_init()
        # hlayout.addWidget(QtWidgets.QPushButton('11'))
        # hwg=QtWidgets.QWidget()
        # hwg.setLayout(hlayout)
        # wlayout.addWidget(hwg)
        # self.setLayout(wlayout)
    def topTab_init(self):
        pass
        # tab1=QLabel(self)
        # tab1.setPixmap(QPixmap('./src/htop_btn_settings.png'))
        # tab1.setGeometry(200, 200, 100,100)
        # tab1.setScaledContents(True)  # 让图片自适应label大小

    def avatar_init(self):
        avatar1 = QLabel(self)
        avatar1.setPixmap(QPixmap('./src/headTopFrame.png'))
        avatar1.setGeometry(2,2, 100, 100)
        avatar1.setScaledContents(True)  # 让图片自适应label大小
        avatar2 = QLabel(self)
        avatar2.setPixmap(QPixmap('./src/headBoy.png'))
        avatar2.setGeometry(7, 7, 90, 90)
        avatar2.setScaledContents(True)  # 让图片自适应label大小
    def userName_init(self):
        name=QLabel(self)
        name.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        name.setText("往事随风")
        name.setGeometry(90,10, 100,25)
        name.setFont(QFont("Microsoft YaHei"))
        name.setStyleSheet("QLabel{color:rgb(255,250,250,255);font-size:20px;font-weight:bold;}")
        zhuyeBtn=QPushButton(self)
        zhuyeBtn.setGeometry(110,60,60,25)
        zhuyeBtn.setStyleSheet("QPushButton{border-image: url(./src/person_btn_tap_zy.png)}")

    def room_init(self):
        level1 = QLabel(self)
        frame1 = QLabel(self)
        frame1.setPixmap(QPixmap('./src/room_frame.png'))
        frame1.setGeometry(150, 200, 170, 225)
        frame1.setScaledContents(True)
        level1.setPixmap(QPixmap('./src/room_bg_level1.png'))
        level1.setGeometry(150, 200, 170, 225)
        level1.setScaledContents(True)  # 让图片自适应label大小

        level2 = QLabel(self)
        level2.setPixmap(QPixmap('./src/room_bg_level2.png'))
        level2.setGeometry(340, 200, 170, 225)
        level2.setScaledContents(True)  # 让图片自适应label大小
        frame2 = QLabel(self)
        frame2.setPixmap(QPixmap('./src/room_frame.png'))
        frame2.setGeometry(340, 200, 170, 225)
        frame2.setScaledContents(True)

        level3 = QLabel(self)
        level3.setPixmap(QPixmap('./src/room_bg_level3.png'))
        level3.setGeometry(530, 200, 170, 225)
        level3.setScaledContents(True)  # 让图片自适应label大小
        frame3 = QLabel(self)
        frame3.setPixmap(QPixmap('./src/room_frame.png'))
        frame3.setGeometry(530, 200, 170, 225)
        frame3.setScaledContents(True)

        level4 = QLabel(self)
        level4.setPixmap(QPixmap('./src/room_bg_level4.png'))
        level4.setGeometry(720, 200, 170, 225)
        level4.setScaledContents(True)  # 让图片自适应label大小
        frame4 = QLabel(self)
        frame4.setPixmap(QPixmap('./src/room_frame.png'))
        frame4.setGeometry(720, 200, 170, 225)
        frame4.setScaledContents(True)

if __name__=="__main__":
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()
    sys.exit(app.exec_())