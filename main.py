import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel, QLineEdit, QTextEdit
from PyQt5.QtGui import QIcon # 아이콘 넣기
from PyQt5.QtCore import QCoreApplication


# 작은 창 하나 띄우기
class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel('날짜'), 0, 0)
        grid.addWidget(QLabel('독서하기'), 1, 0)
        grid.addWidget(QLabel('운동하기'), 2, 0)
        grid.addWidget(QLabel('글쓰기'), 3, 0)

        self.setWindowTitle('Elastic Habits')  # 창의 제목
        self.setWindowIcon(QIcon('icon.png'))  # 아이콘 넣기
        self.setGeometry(300, 300, 1366, 768)  # 창의 위치(앞에 2개)와 크기(뒤에 2개) move + resize 합친 것과 같음
        # self.move(300, 300)  # 위젯을 스크린의 x=300px, y=300px (아직 모르겠음)
        # self.resize(400, 200)  # 위젯의 크기
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
