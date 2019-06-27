# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFont


class StackedExample(QWidget):
    def __init__(self):
        super(StackedExample, self).__init__()
        # 设置窗口初始位置和大小
        self.setGeometry(500, 400, 800, 400)
        self.setWindowTitle('StackedWidget 例子')
        # 创建列表窗口，添加条目
        self.leftlist()
        # 创建三个小控件
        self.stack1 = QWidget()
        self.stack1.setStyleSheet("QWidget{border-left:1px solid #D6D8DD;border-bottom:1px solid #D6D8DD}")
        self.stack2 = QWidget()
        self.stack2.setStyleSheet("QWidget{border-left:1px solid #D6D8DD;border-bottom:1px solid #D6D8DD}")
        self.stack3 = QWidget()
        self.stack3.setStyleSheet("QWidget{border-left:1px solid #D6D8DD;border-bottom:1px solid #D6D8DD}")
        self.show_money = QWidget()
        self.show_money.setStyleSheet("QWidget{border-left:1px solid #D6D8DD;}")
        # self.line = QFrame.HLine()

        # 创建三个小控件对应的UI
        self.stack1UI()
        self.stack2UI()
        self.stack3UI()
        self.show_money_UI()

        # 在QStackedWidget对象中填充了三个子控件
        self.stack = QStackedWidget(self)
        self.stack.addWidget(self.stack1)
        self.stack.addWidget(self.stack2)
        self.stack.addWidget(self.stack3)

        # 全局水平布局，左侧列表，右侧垂直布局添加部件到布局中
        mainbox = QHBoxLayout(self, spacing=0)
        mainbox.setContentsMargins(0, 0, 0, 0)
        vbox = QVBoxLayout()
        vbox.addWidget(self.stack)
        vbox.addWidget(self.show_money)

        # vbox.setStretchFactor(self.stack, 1)
        # vbox.setStretchFactor(self.show_money, 1)
        mainbox.addWidget(self.leftlist)
        mainbox.addLayout(vbox)
        self.setLayout(mainbox)
        self.leftlist.currentRowChanged.connect(self.display)
        self.init()
    #     self.first_blue()
    # def first_blue(self):
    #     if self.leftlist.currentItem == 1:
    #         print(self.leftlist.currentItem)

    def leftlist(self):

        self.leftlist = QListWidget()
        self.leftlist.setFrameShape(QListWidget.NoFrame)
        with open('stackqss.qss', 'r') as f:  # 导入QListWidget的qss样式
            self.list_style = f.read()
        self.leftlist.setStyleSheet(self.list_style)
        list_str = ['客户信息', '温度', '湿度']

        for i in range(3):
            self.item = QListWidgetItem(list_str[i], self.leftlist)  # 左侧选项的添加
            self.item.setSizeHint(QSize(110, 60))
            self.item.setFont(QFont('微软雅黑', 10))
            self.item.setTextAlignment(Qt.AlignCenter)  # 居中显示

    def init(self):
        self.blytwdb.clicked.connect(self.set0)

    def show_money_UI(self):
        style1 = "QLabel{color:black;font-size:13px;font-family:Microsoft YaHei}"
        style2 = "QLineEdit{color:black;font-size:13px;font-family:Microsoft YaHei}"
        money_layout = QGridLayout()
        temp = QLabel('温度检定（校准）费用:')
        temp.setStyleSheet(style1)
        humi = QLabel('  湿度检定（校准）费用:')
        humi.setStyleSheet(style1)
        wind = QLabel('   风检定（校准）费用:')
        wind.setStyleSheet(style1)
        pressure = QLabel('气压检定（校准）费用:')
        pressure.setStyleSheet(style1)
        rain = QLabel('  雨量检定（校准）费用:')
        rain.setStyleSheet(style1)
        radi = QLabel('辐射检定（校准）费用:')
        radi.setStyleSheet(style1)
        other = QLabel('             其它业务费用:')
        other.setStyleSheet(style1)
        total_money = QLabel("检定（校准）费用总计:")
        total_money.setStyleSheet(style1)
        self.temp_text = QLineEdit()
        self.temp_text.setStyleSheet(style2)
        self.temp_text.setAlignment(QtCore.Qt.AlignCenter)
        self.humi_text = QLineEdit()
        self.humi_text.setStyleSheet(style2)
        self.humi_text.setAlignment(QtCore.Qt.AlignCenter)
        self.wind_text = QLineEdit()
        self.wind_text.setStyleSheet(style2)
        self.wind_text.setAlignment(QtCore.Qt.AlignCenter)
        self.pressure_text = QLineEdit()
        self.pressure_text.setStyleSheet(style2)
        self.pressure_text.setAlignment(QtCore.Qt.AlignCenter)
        self.rain_text = QLineEdit()
        self.rain_text.setStyleSheet(style2)
        self.rain_text.setAlignment(QtCore.Qt.AlignCenter)
        self.radi_text = QLineEdit()
        self.radi_text.setStyleSheet(style2)
        self.radi_text.setAlignment(QtCore.Qt.AlignCenter)
        self.other_text = QLineEdit()
        self.other_text.setStyleSheet(style2)
        self.other_text.setAlignment(QtCore.Qt.AlignCenter)
        self.total_money = QLineEdit()
        self.total_money.setStyleSheet(style2)
        self.total_money.setAlignment(QtCore.Qt.AlignCenter)
        money_layout.setSpacing(10)
        money_layout.addWidget(temp, 1, 1, 1, 1)
        money_layout.addWidget(self.temp_text, 1, 2, 1, 1)
        money_layout.addWidget(humi, 1, 3, 1, 1)
        money_layout.addWidget(self.humi_text, 1, 4, 1, 1)
        money_layout.addWidget(wind, 1, 5, 1, 1)
        money_layout.addWidget(self.wind_text, 1, 6, 1, 1)
        money_layout.addWidget(pressure, 2, 1, 1, 1)
        money_layout.addWidget(self.pressure_text, 2, 2, 1, 1)

        money_layout.addWidget(rain, 2, 3, 1, 1)
        money_layout.addWidget(self.rain_text, 2, 4, 1, 1)
        money_layout.addWidget(radi, 2, 5, 1, 1)
        money_layout.addWidget(self.radi_text, 2, 6, 1, 1)
        money_layout.addWidget(other, 3, 1, 1, 1)
        money_layout.addWidget(self.other_text, 3, 2, 1, 1)
        money_layout.addWidget(total_money, 3, 5, 1, 1)
        money_layout.addWidget(self.total_money, 3, 6, 1, 1)
        money_layout.setContentsMargins(10, 20, 20, 30)

        self.show_money.setLayout(money_layout)

    def stack1UI(self):
        layout1 = QGridLayout()
        # 设置字体
        style1 = "QLabel{color:black;font-size:13px;font-family:Microsoft YaHei}"
        style2 = "QLineEdit{color:black;font-size:13px;font-family:Microsoft YaHei}"
        # 公司名称的label
        label1 = QLabel("公司名称:")
        label1.setStyleSheet(style1)
        # 公司名称的lineedit
        self.company_name = QLineEdit()
        self.company_name.setStyleSheet(style2)
        layout1.addWidget(label1, 1, 1, 1, 1)
        layout1.addWidget(self.company_name, 1, 2, 1, 8)
        # 联系地址的label
        label2 = QLabel("联系地址:")
        label2.setStyleSheet(style1)
        # 联系地址的lineedit
        self.company_address = QLineEdit()
        self.company_address.setStyleSheet(style2)
        layout1.addWidget(label2, 2, 1, 1, 1)
        layout1.addWidget(self.company_address, 2, 2, 1, 8)
        # 联系电话的label
        label3 = QLabel("联系电话:")
        label3.setStyleSheet(style1)
        # 联系电话的lineedit
        self.company_tel = QLineEdit()
        self.company_tel.setStyleSheet(style2)
        self.company_tel.setContentsMargins(0,0,20,0)
        layout1.addWidget(label3, 3, 1, 1, 1)
        layout1.addWidget(self.company_tel, 3, 2, 1, 1)
        # layout1.setSpacing(5)
        # layout1.getItemPosition(1000)
        # layout1.setHorizontalSpacing(200)
        layout1.setContentsMargins(28, 19, 30, 0)
        # layout1.setContentsMargins(28, 19, 30, 50)
        self.stack1.setLayout(layout1)

    def stack2UI(self):
        # 主表单布局，次水平布局
        layout = QGridLayout()
        style1 = "QLabel{color:black;font-size:13px;font-family:Microsoft YaHei}"
        style2 = "QLineEdit{color:black;font-size:13px;font-family:Microsoft YaHei}"
        self.blytwdb = QPushButton()
        self.blytwdb.setFixedSize(90, 90)
        self.blytwdb.setText("气象用玻璃\n液体温度表")

        self.sjswdj = QPushButton()
        self.sjswdj.setText("气象用双金\n属温度计")
        self.sjswdj.setFixedSize(90, 90)

        self.wdcgq = QPushButton()
        self.wdcgq.setText("自动站温度\n传感器")
        self.wdcgq.setFixedSize(90, 90)

        self.bdz = QPushButton("铂电阻")
        self.bdz.setFixedSize(90, 90)
        self.pr630 = QLabel("630元/支")
        self.pr630_1 = QLabel("630元/支")
        self.pr1000 = QLabel("1000元/支")
        self.pr1120 = QLabel("1120元/支")

        layout.addWidget(self.blytwdb, 1, 1, 1, 1)
        layout.addWidget(self.sjswdj, 1, 2, 1, 1)
        layout.addWidget(self.wdcgq, 1, 3, 1, 1)
        layout.addWidget(self.bdz, 1, 4, 1, 1)
        layout.addWidget(self.pr630, 2, 1, 1, 1)
        layout.addWidget(self.pr630_1, 2, 2, 1, 1)
        layout.addWidget(self.pr1000, 2, 3, 1, 1)
        layout.addWidget(self.pr1120, 2, 4, 1, 1)
        layout.setContentsMargins(28, 19, 30, 0)
        self.stack2.setLayout(layout)

    def set0(self):
        self.bir.setText('nan')
        self.name.setText('nan')

    def stack3UI(self):
        # 水平布局
        layout = QHBoxLayout()
        # 添加控件到布局中
        layout.addWidget(QLabel('科目'))
        layout.addWidget(QCheckBox('物理'))
        layout.addWidget(QCheckBox('高数'))

        self.stack3.setLayout(layout)

    def display(self, i):
        # 设置当前可见的选项卡的索引
        self.stack.setCurrentIndex(i)
        # if i == 0:
        #     self.leftlist.setStyleSheet(self.list_style)
        #     self.item = QListWidgetItem('客户信息', self.leftlist)  # 左侧选项的添加
        #     self.item.setSizeHint(QSize(110, 60))
        #     self.item.setFont(QFont('微软雅黑', 10))
        #     self.item.setTextAlignment(Qt.AlignCenter)

    def man(self):
        self.name.setText("fff")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = StackedExample()
    demo.show()
    sys.exit(app.exec_())