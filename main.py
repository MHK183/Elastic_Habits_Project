import sys, pickle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon # 아이콘 넣기
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.row = 5
        self.col = 18
        self.initUI()

    def initUI(self):

        self.setWindowTitle('Elastic Habits')  # 창의 제목
        self.setWindowIcon(QIcon('icon.png'))  # 아이콘 넣기
        self.setGeometry(300, 300, 1366, 768)  # 창의 위치(앞에 2개)와 크기(뒤에 2개) move + resize 합친 것과 같음

        # 테이블 생성 및 저장 버튼
        self.createTable()
        self.createTable2()
        self.btn = QPushButton('저장')
        self.btn.clicked.connect(on_cl)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.table)
        self.layout.addWidget(self.table2)
        self.layout.addWidget(self.btn)

        self.setLayout(self.layout)
        self.show()

    def createTable(self):
        self.table = QTableWidget()
        self.table.setRowCount(self.row)
        self.table.setColumnCount(self.col)

        # 열 너비 조정
        for i in range(self.col):
            self.table.setColumnWidth(i, 1)
            if i >= 15:
                self.table.setColumnWidth(i, 80)
        # 마지막 행 높이 조정
        self.table.setRowHeight(4, 55)
        # 열 및 행 제목 리스트 저장
        col_headers = [str(i) for i in range(1, 15 + 1)] + ['미니', '플러스', '엘리트']
        row_indexes = ['독서하기', '운동하기', '글쓰기', '', '']
        # 열 및 행 제목 생성
        self.table.setHorizontalHeaderLabels(col_headers)
        self.table.setVerticalHeaderLabels(row_indexes)

        try:
            fp = open("out.txt", "rb")
            for r in range(self.row):
                for c in range(self.col):
                    self.table.setItem(r, c, QTableWidgetItem(str(pickle.load(fp))))
            fp.close()
        except:
            for r in range(self.row):
                for c in range(self.col):
                    self.table.setItem(r, c, QTableWidgetItem(""))

        # 특정 칸 값 지정
        score_titles = ['미니\n총점', '플러스\n총점', '엘리트\n총점']
        for i in range(3):
            item = QTableWidgetItem(score_titles[i])
            item.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(4, i+15, item)

    def createTable2(self):
        self.table2 = QTableWidget()
        self.table2.setRowCount(self.row)
        self.table2.setColumnCount(self.col)

        # 열 너비 조정
        for i in range(self.col):
            self.table2.setColumnWidth(i, 1)
            if i >= 15:
                self.table2.setColumnWidth(i, 80)
        # 마지막 행 높이 조정
        self.table2.setRowHeight(4, 55)
        # 열 및 행 제목 리스트 저장
        col_headers = [str(i) for i in range(16, 30 + 1)] + ['미니', '플러스', '엘리트']
        row_indexes = ['독서하기', '운동하기', '글쓰기', '', '']
        # 열 및 행 제목 생성
        self.table2.setHorizontalHeaderLabels(col_headers)
        self.table2.setVerticalHeaderLabels(row_indexes)

        try:
            fp = open("out.txt", "rb")
            for r in range(self.row):
                for c in range(self.col):
                    self.table2.setItem(r, c, QTableWidgetItem(str(pickle.load(fp))))
            fp.close()
        except:
            for r in range(self.row):
                for c in range(self.col):
                    self.table2.setItem(r, c, QTableWidgetItem(""))

        # 특정 칸 값 지정
        score_titles = ['미니\n총점', '플러스\n총점', '엘리트\n총점']
        for i in range(3):
            item = QTableWidgetItem(score_titles[i])
            item.setTextAlignment(Qt.AlignCenter)
            self.table2.setItem(4, i+15, item)

# 저장 함수
def on_cl():
    fp = open("out.txt", "wb")
    for r in range(ex.row):
        for c in range(ex.col):
            pickle.dump(ex.table.item(r, c).text(), fp)
    fp.close()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


