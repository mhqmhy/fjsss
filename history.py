import sys
from historyListUi import Ui_Form
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QLabel,QPushButton,QListWidget,QVBoxLayout,QHBoxLayout,QTableWidget,QTableWidgetItem,QScrollArea,QHeaderView
from PyQt5.QtGui import QMovie,QPixmap,QCursor,QPalette,QBrush,QFont,QIcon
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
import random

class History(Ui_Form,QWidget):
    def __init__(self):
        super(History,self).__init__()
        self.setupUi(self)
        self.initUi()
        self.updateRecords()
    def initUi(self):
        self.historyList = QListWidget()
        self.historyDetail=QTableWidget(3,2)
        hbox =QHBoxLayout()
        hbox.addWidget(self.historyList)
        self.labelWidget=QScrollArea()
        vbox = QVBoxLayout()
        vbox.addWidget(self.historyDetail)
        vbox.addWidget(self.labelWidget)
        x=QWidget()
        x.setLayout(vbox)
        hbox.addWidget(x)
        self.setLayout(hbox)
        self.historyList.setStyleSheet("background-color:transparent")  # 只能用这个
        self.historyDetail.setStyleSheet("background-color:transparent")

        self.historyDetail.horizontalHeader().setVisible(False)
        self.historyDetail.verticalHeader().setVisible(False)
        # TODO 优化设置表格为自适应的伸缩模式
        self.historyDetail.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.historyDetail.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.historyDetail.verticalHeader().setStyleSheet("background-color:transparent")
    def updateRecords(self):
        self.historyList.addItem('item1')
        x = QTableWidgetItem()
        x.setText('玩家ID')
        self.historyDetail.setItem(0,0,x)
        y = QTableWidgetItem()
        y.setText('用户名')
        self.historyDetail.setItem(1,0, y)
        z = QTableWidgetItem()
        z.setText('得分')
        self.historyDetail.setItem(2, 0, z)
        # x=QTableWidgetItem()
        # x.setText('q')
        # self.historyDetail.setItem(1,1,x)

if __name__=="__main__":
    app = QApplication(sys.argv)
    demo = History()
    demo.show()
    sys.exit(app.exec_())