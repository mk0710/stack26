# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize, Qt, QRect
from PyQt5.QtGui import QFont


class StackedExample(QWidget):
    def __init__(self):
        super(StackedExample, self).__init__()
        # 设置窗口初始位置和大小
        self.setGeometry(300, 300, 650, 400)
        self.setWindowTitle('StackedWidget 例子')

        # 创建列表窗口，添加条目
        self.leftlist()

        # 创建三个小控件
        self.stack1 = QWidget()
        self.stack1.setStyleSheet("QWidget{border-left:1px solid #D6D8DD}")
        self.stack2 = QWidget()
        self.stack2.setStyleSheet("QWidget{border-left:1px solid #D6D8DD}")
        self.stack3 = QWidget()

        self.stack3.setStyleSheet("QWidget{;border-left:1px solid #D6D8DD}")
        self.show_money = QWidget()
        self.show_money.setStyleSheet("QWidget{border-left:1px solid #D6D8DD}")

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
        vbox.setContentsMargins(0, 0,25,0)

        vbox.addWidget(self.stack)

        vbox.addWidget(self.show_money)

        mainbox.addWidget(self.leftlist)
        mainbox.addLayout(vbox)
        self.setLayout(mainbox)
        self.leftlist.currentRowChanged.connect(self.display)
        self.init()

    def leftlist(self):

        self.leftlist = QListWidget()
        self.leftlist.setFrameShape(QListWidget.NoFrame)
        with open('stackqss.qss', 'r') as f:  # 导入QListWidget的qss样式
            self.list_style = f.read()
        self.leftlist.setStyleSheet(self.list_style)
        # self.leftlist.setStyleSheet("QListWidget{min-width:80px; max-width:180px; border:0px solid gray; color:black}"
        #                                # "QListWidget::Item{padding-top:20px; padding-bottom:4px}"
        # "QListWidget::Item:selected{color: black; border-left: 5px solid rgb(0, 120, 215)}"  )
        list_str = ['客户信息', '温度', '湿度']

        for i in range(3):
            self.item = QListWidgetItem(list_str[i], self.leftlist)  # 左侧选项的添加
            self.item.setSizeHint(QSize(30, 60))
            self.item.setFont(QFont('微软雅黑', 10))
            self.item.setTextAlignment(Qt.AlignCenter)  # 居中显示

    def init(self):
        self.male_btn.clicked.connect(self.set0)

    def show_money_UI(self):
        money_layout = QGridLayout()
        formlayout = QFormLayout()
        total_money = QLabel("总金额:")
        total_money.setStyleSheet("QLabel{color:black;"
                                  "font-size:15px;"
                                  "border-left:1px solid #D6D8DD;"
                                  "font-family:Microsoft YaHei}")
        self.total_money = QLineEdit()
        self.total_money.setStyleSheet("QLineEdit{color:black;"
                                       "font-size:15px;"
                                       "border-left:1px solid #D6D8DD;"
                                       "font-family:Microsoft YaHei}")
        formlayout.addRow(total_money, self.total_money)
        formlayout.setContentsMargins(0,0,100,0)
        self.show_money.setLayout(formlayout)

    def stack1UI(self):
        layout1 = QFormLayout()

        label1 = QLabel("公司名称:")
        # 设置公司名称的字体
        label1.setStyleSheet("QLabel{color:black;"
                             "font-size:15px;"
                             "border-left:1px solid #D6D8DD;"
                             # "font-weight:bold;"
                             "font-family:Microsoft YaHei}")
        self.company_name = QLineEdit()
        # 设置公司名称LineEdit字体
        self.company_name.setStyleSheet("QLineEdit{color:black;"
                                        "font-size:15px;"
                                        "border-left:1px solid #D6D8DD;"
                                        "font-family:Microsoft YaHei}")
        layout1.addRow(label1, self.company_name)
        # 设置联系地址的字体
        label2 = QLabel("联系地址:")

        label2.setStyleSheet("QLabel{color:black;"
                             "font-size:15px;"
                             "border-left:1px solid #D6D8DD;"
                             "font-family:Microsoft YaHei}")
        self.company_address = QLineEdit()
        # 设置公司名称LineEdit字体
        self.company_address.setStyleSheet("QLineEdit{color:black;"
                                           "font-size:15px;"
                                           "border-left:1px solid #D6D8DD;"
                                           "font-family:Microsoft YaHei}")
        layout1.addRow(label2, self.company_address)

        layout1.setSpacing(15)
        # layout1.getItemPosition(1000)
        layout1.setHorizontalSpacing(15)
        layout1.sizeHint()
        self.stack1.setLayout(layout1)


    def stack2UI(self):
        # 主表单布局，次水平布局
        self.male_btn = QPushButton("男")
        layout = QFormLayout()
        sex = QHBoxLayout()
        # 水平布局添加单选按钮
        sex.addWidget(self.male_btn)
        self.male_btn.setStyleSheet(''' text-align : center;
                                   background-color : DarkSeaGreen;
                                   height : 20px;
                                   
                                   border-width: 1px;
                                   border-color: rgb(255, 0, 0);                  
                                   font : 20pt;
                                   font-family:Microsoft YaHei 
                                    ''')

        sex.addWidget(QRadioButton('女'))

        # 表单布局添加控件
        layout.addRow(QLabel('性别'), sex)
        self.bir = QLineEdit()
        layout.addRow('生日', self.bir)
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

    def man(self):

        self.name.setText("fff")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = StackedExample()
    demo.show()
    sys.exit(app.exec_())