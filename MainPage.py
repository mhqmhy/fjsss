import sys
from MainPageUi import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow
from PyQt5.QtGui import QMovie,QPixmap,QCursor,QPalette,QBrush

class MainWindow(QMainWindow,Ui_MainWindow):

    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        #self.setMinimumSize(1680, 1136)
        self.setMinimumSize(720, 487)
        self.setMaximumSize(1680, 1136)
        self.setStyleSheet("#MainWindow{border-image:url(./src/hall.jpg);}")
        # palette = QPalette()
        # palette.setBrush(self.backgroundRole(), QBrush(QPixmap('./src/hall.jpg')))
        # self.setPalette(palette)
        self.setCursor(QCursor(QPixmap('./src/mouse40.png')))

    def initUi(self):
        pass



if __name__=="__main__":
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()
    sys.exit(app.exec_())