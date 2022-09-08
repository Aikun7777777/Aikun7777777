#  用pyqt制作一个图片列表
import os
import shutil
import sys

from PyQt5.QtCore import QTimer, QDateTime
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMainWindow, QListWidget, QApplication, QLabel, QPushButton, QFileDialog, QDialog


# path = r'E:\CV04\0823\20220819\Original\NG'
#
# ng_path = path
# img_list = os.listdir(ng_path)
# print(img_list)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        btn = QPushButton('原图路径', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(30, 50)       # 设置按钮的位置
        self.img_list = []
        btn.clicked.connect(self.click_choice_dir)

        atn = QPushButton('过杀', self)
        atn.setToolTip('This is a <b>QPushButton</b> widget')
        atn.resize(atn.sizeHint())
        atn.move(200, 50)  # 设置按钮的位置
        self.over_kill_list = []
        atn.clicked.connect(self.move_over_kill)

        ctn = QPushButton('漏杀', self)
        ctn.setToolTip('This is a <b>QPushButton</b> widget')
        ctn.resize(ctn.sizeHint())
        ctn.move(370, 50)  # 设置按钮的位置
        ctn.clicked.connect(self.escape_kill)

        #退出按钮
        # self.setGeometry(540, 50, 250, 150)   # 定义窗口的位置和大小
        # self.setWindowTitle('Quit button')
        # self.show()
        quit = QPushButton('Quit', self)
        quit.setGeometry(540, 50, 100, 30)
        quit.clicked.connect(QApplication.instance().quit)

        self.setWindowTitle("章鱼博士SPC--过漏杀")   #时间
        self.setWindowIcon(QIcon('1.ico'))
        self.label = QLabel(self)
        self.label.setFixedWidth(300)  # 设置label的宽度
        self.label.move(300, -10)  # 设置label的位置
        self.label.setStyleSheet("QLabel{background:white;}"
                                 "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}"
                                 )
        # 动态显示时间在label上
        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start()
        self.resize(1600,1000)
        self.setup_ui()

    def showtime(self):
        datetime = QDateTime.currentDateTime()
        text = datetime.toString()
        self.label.setText("     " + text)



    def click_choice_dir(self):
        self.dir_path = QFileDialog.getExistingDirectory(self, "请选择文件夹路径", "E:\CV04\yolov5-6.0housesmart\data\images")
        self.img_list = os.listdir(self.dir_path)
        self.list_widget.addItems(self.img_list)
        print(self.dir_path)
        print(self.img_list)

    def setup_ui(self):
        self.lab1 = QLabel(self)  # 设置图片显示label
        self.lab1.setText("显示图片")
        self.lab1.setFixedSize(800, 500)  # 设置图片大小
        self.lab1.move(300, 100)  # 设置图片位置
        self.lab1.setStyleSheet("QLabel{background:white;}")

        self.list_widget = QListWidget(self)
        self.list_widget.resize(200,200)    #设置列表大小
        self.list_widget.move(10,100)
        # self.list_widget.addItems(self.img_list)
        self.list_widget.itemClicked.connect(self.list_widget_click)

        self.voer_kill = QLabel(self)
        self.voer_kill.setFixedSize(80, 50)  # 设置图片大小
        self.voer_kill.move(20, 50)  # 设置图片位置
        self.voer_kill.setStyleSheet("QLabel{background:white;}")

    #展示点击图片
    def list_widget_click(self,item):
        print(item.text())
        img_path = self.dir_path + '//' + item.text()
        print(img_path)
        self.showImage = QPixmap(img_path).scaled(self.lab1.width(), self.lab1.height())  # 适应窗口大小
        self.lab1.setPixmap(self.showImage)  # 显示图片

    def move_over_kill(self):     #过杀
        os.makedirs(os.path.join(self.dir_path, 'over_kill'), exist_ok=True)
        selectedItem = self.list_widget.selectedItems()[0].text()
        shutil.copy(os.path.join(self.dir_path, selectedItem), self.dir_path + '//' + 'over_kill')

        #展示成果

    def escape_kill(self):
        os.makedirs(os.path.join(self.dir_path, 'escape_kill'), exist_ok=True)
        selectedItem2 = self.list_widget.selectedItems()[0].text()
        shutil.copy(os.path.join(self.dir_path, selectedItem2), self.dir_path + '//' + 'escape_kill')
        #展示成果

class showTime(QDialog):
    def __init__(self):

        super(showTime, self).__init__()
        self.resize(500, 400)
        self.setWindowTitle("label显示时间")
        self.label = QLabel(self)
        self.label.setFixedWidth(200)   # 设置label的宽度
        self.label.move(900, 80)        # 设置label的位置
        self.label.setStyleSheet("QLabel{background:white;}"
"QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}"
                                      )
        # 动态显示时间在label上
        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start()
    def showtime(self):
        datetime = QDateTime.currentDateTime()
        text = datetime.toString()
        self.label.setText("     "+ text)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    # window = showTime()
    window.show()
    sys.exit(app.exec_())