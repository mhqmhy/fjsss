import sys
from historyListUi import Ui_Form
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget,QAbstractItemView,QLabel,QLineEdit,QPushButton,QListWidget,QVBoxLayout,QHBoxLayout,QTableWidget,QTableWidgetItem,QScrollArea,QHeaderView
from PyQt5.QtGui import QMovie,QPixmap,QCursor,QPalette,QBrush,QFont,QIcon
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
import random



class History(Ui_Form,QWidget):
    def __init__(self):
        super(History,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("历史战局记录")
        self.initUi()
        self.init_HistoryDetail()
        self.showPokes()
    def initUi(self):
        label1=QLabel(self)
        label1.setText("玩家ID")
        lineEdit=QLineEdit(self)
        hboxx=QHBoxLayout()
        hboxx.addWidget(label1)
        hboxx.addWidget(lineEdit)
        ww=QWidget()
        ww.setLayout(hboxx)
        self.historyList = QListWidget()
        self.historyDetail=QTableWidget(4,2) #初始化表格大小
        hbox =QHBoxLayout()
        hbox.addWidget(self.historyList)
        self.labelWidget=QScrollArea()
        vbox = QVBoxLayout()
        vbox.addWidget(ww)
        vbox.addWidget(QPushButton("确定"))
        vbox.addWidget(self.historyDetail)
        vbox.addWidget(self.labelWidget)
        x=QWidget()
        x.setLayout(vbox)
        hbox.addWidget(x)
        self.setLayout(hbox)
        self.historyList.setStyleSheet("background-color:transparent")  # 只能用这个
        self.historyDetail.setStyleSheet("background-color:transparent")
        #设置表头不可见
        self.historyDetail.horizontalHeader().setVisible(False)
        self.historyDetail.verticalHeader().setVisible(False)
        # TODO 优化设置表格为自适应的伸缩模式
        self.historyDetail.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.historyDetail.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.historyDetail.verticalHeader().setStyleSheet("background-color:transparent")

    def tableAddItem(self,text): #给self.historyDetail添加值
        x = QTableWidgetItem()
        x.setText(text)
        x.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        return x

    def init_HistoryDetail(self):
        self.historyDetail.setEditTriggers(QAbstractItemView.NoEditTriggers) #设置表格不可编辑
        self.historyDetail.setItem(0,0,self.tableAddItem('战局ID'))
        self.historyDetail.setItem(1,0,self.tableAddItem('结算时间'))
        self.historyDetail.setItem(2,0,self.tableAddItem('玩家昵称/ID'))
        self.historyDetail.setItem(3,0,self.tableAddItem('得分变化'))
    def LabelWidgetAddPoke(self,text=None):
        a = QLabel()
        a.setPixmap(QPixmap('./src/cardBack.png'))
        a.setMaximumSize(48,66)
        a.setMinimumSize(48,66)
        a.setScaledContents(True)
        return a
    def showPokes(self):
        qianDun=QHBoxLayout()
        qianDun.addWidget(self.LabelWidgetAddPoke())
        qianDun.addWidget(self.LabelWidgetAddPoke())
        qianDun.addWidget(self.LabelWidgetAddPoke())
        zhongDun=QHBoxLayout()
        zhongDun.addWidget(self.LabelWidgetAddPoke())
        zhongDun.addWidget(self.LabelWidgetAddPoke())
        zhongDun.addWidget(self.LabelWidgetAddPoke())
        zhongDun.addWidget(self.LabelWidgetAddPoke())
        zhongDun.addWidget(self.LabelWidgetAddPoke())
        houDun=QHBoxLayout()
        houDun.addWidget(self.LabelWidgetAddPoke())
        houDun.addWidget(self.LabelWidgetAddPoke())
        houDun.addWidget(self.LabelWidgetAddPoke())
        houDun.addWidget(self.LabelWidgetAddPoke())
        houDun.addWidget(self.LabelWidgetAddPoke())
        pokeLayout=QVBoxLayout()
        X=QWidget()
        Y=QWidget()
        Z=QWidget()
        X.setLayout(qianDun)
        Y.setLayout(zhongDun)
        Z.setLayout(houDun)
        pokeLayout.addWidget(X)
        pokeLayout.addWidget(Y)
        pokeLayout.addWidget(Z)
        self.labelWidget.setLayout(pokeLayout)
    def update_HistoryList(self):
        pass
if __name__=="__main__":
    app = QApplication(sys.argv)
    demo = History()
    demo.show()
    sys.exit(app.exec_())