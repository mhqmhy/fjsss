import sys
from historyListUi import Ui_Form
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QLabel,QPushButton,QListWidget,QVBoxLayout,QHBoxLayout,QTableWidget,QTableWidgetItem,QScrollArea,QHeaderView
from PyQt5.QtGui import QMovie,QPixmap,QCursor,QPalette,QBrush,QFont,QIcon
from PyQt5 import QtCore
from PyQt5.QtCore import Qt


class RankList(QWidget):

    def __init__(self):
        super(RankList,self).__init__()
        vbox=QVBoxLayout()
        self.rankingList=QListWidget()
        vbox.addWidget(self.rankingList)
        self.setLayout(vbox)
    def updateItems(self):
        pass

if __name__=="__main__":
    app = QApplication(sys.argv)
    demo = RankList()
    demo.show()
    sys.exit(app.exec_())