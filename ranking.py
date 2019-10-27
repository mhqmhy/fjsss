import sys
from historyListUi import Ui_Form
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QLabel,QPushButton,QListWidget,QVBoxLayout,QHBoxLayout,QTableWidget,QTableWidgetItem,QScrollArea,QHeaderView,QAbstractItemView
from PyQt5.QtGui import QMovie,QPixmap,QCursor,QPalette,QBrush,QFont,QIcon
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
import requests,json

class RankList(QWidget):

    def __init__(self):
        super(RankList,self).__init__()
        self.setWindowTitle('排行榜')
        url = 'http://api.revth.com/rank'
        re = requests.get(url)
        self.rank_json = json.loads(re.text)
        vbox=QVBoxLayout()
        self.rankingList=QTableWidget(len(self.rank_json)+1,4)
        self.rankingList.setSelectionBehavior(QAbstractItemView.SelectRows) #
        # self.rankingList.setSelectionMode(QAbstractItemView.SingleSelection) # 设置选择模式，选择单行
        vbox.addWidget(self.rankingList)
        self.setLayout(vbox)
        self.rankingList.setStyleSheet("background-color:transparent")
        # 设置表头不可见
        self.rankingList.horizontalHeader().setVisible(False)
        self.rankingList.verticalHeader().setVisible(False)
        # TODO 优化设置表格为自适应的伸缩模式
        self.rankingList.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.rankingList.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.updateItems()

    def tableAddItem(self, text):  # 给self.historyDetail添加值
        x = QTableWidgetItem()
        x.setText(text)
        x.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        return x
    def updateItems(self):
        self.rankingList.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 设置表格不可编辑
        self.rankingList.setItem(0, 0, self.tableAddItem('排名'))
        self.rankingList.setItem(0, 1, self.tableAddItem('玩家ID'))
        self.rankingList.setItem(0, 2, self.tableAddItem('玩家名'))
        self.rankingList.setItem(0, 3, self.tableAddItem('玩家得分'))
        for i in self.rank_json:
            self.rankingList.setItem(1+self.rank_json.index(i), 0, self.tableAddItem(str(1+self.rank_json.index(i))))
            self.rankingList.setItem(1+self.rank_json.index(i),1,self.tableAddItem(str(i["player_id"])))
            self.rankingList.setItem(1 + self.rank_json.index(i), 2, self.tableAddItem(i["name"]))
            self.rankingList.setItem(1 + self.rank_json.index(i),3, self.tableAddItem(str(i["score"])))
if __name__=="__main__":
    app = QApplication(sys.argv)
    demo = RankList()
    demo.show()
    sys.exit(app.exec_())