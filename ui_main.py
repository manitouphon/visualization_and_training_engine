from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 500)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(14)
        self.Top_Bar.setFont(font)
        self.Top_Bar.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QFrame.Shape.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Shadow.Raised)
        self.Top_Bar.setObjectName("Top_Bar")
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_menu = QFrame(self.Top_Bar)
        self.frame_menu.setMaximumSize(QSize(70, 40))
        self.frame_menu.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.frame_menu.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_menu.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_menu.setObjectName("frame_menu")
        self.verticalLayout_2 = QVBoxLayout(self.frame_menu)
        self.verticalLayout_2.setContentsMargins(15, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Btn_Toggle = QPushButton(self.frame_menu)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setMaximumSize(QSize(40, 16777215))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.Btn_Toggle.setFont(font)
        self.Btn_Toggle.setStyleSheet("background-color: rgb(0,0,0);\n"
"border: 0px solid;")
        self.Btn_Toggle.setText("")
        icon = QIcon()
        icon.addPixmap(QPixmap("icons/menu-svgrepo-com.svg"), QIcon.Mode.Normal, QIcon.State.Off)
        self.Btn_Toggle.setIcon(icon)
        self.Btn_Toggle.setIconSize(QSize(60, 60))
        self.Btn_Toggle.setObjectName("Btn_Toggle")
        self.verticalLayout_2.addWidget(self.Btn_Toggle)
        self.horizontalLayout.addWidget(self.frame_menu)
        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_top.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout.addWidget(self.frame_top)
        self.verticalLayout.addWidget(self.Top_Bar)
        self.Content = QFrame(self.centralwidget)
        self.Content.setFrameShape(QFrame.Shape.NoFrame)
        self.Content.setFrameShadow(QFrame.Shadow.Raised)
        self.Content.setObjectName("Content")
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setMinimumSize(QSize(200, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.frame_left_menu.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_top_menus.setObjectName("frame_top_menus")
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_Visualization = QPushButton(self.frame_top_menus)
        self.btn_Visualization.setMinimumSize(QSize(0, 60))
        font = QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        font.setBold(True)
        self.btn_Visualization.setFont(font)
        self.btn_Visualization.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 113, 165);\n"
"    border-radius: 10px ;\n"
"    margin: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addPixmap(QPixmap("icons/graph-svgrepo-com.svg"), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_Visualization.setIcon(icon1)
        self.btn_Visualization.setIconSize(QSize(30, 30))
        self.btn_Visualization.setObjectName("btn_Visualization")
        self.verticalLayout_4.addWidget(self.btn_Visualization)
        self.btn_learning = QPushButton(self.frame_top_menus)
        self.btn_learning.setMinimumSize(QSize(0, 60))
        font = QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        font.setBold(True)
        self.btn_learning.setFont(font)
        self.btn_learning.setStyleSheet("QPushButton {\n"
"    background-color: rgb(0, 113, 165);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px ;\n"
"    margin: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addPixmap(QPixmap("icons/big-data-svgrepo-com.svg"), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_learning.setIcon(icon2)
        self.btn_learning.setIconSize(QSize(30, 30))
        self.btn_learning.setObjectName("btn_learning")
        self.verticalLayout_4.addWidget(self.btn_learning)
        self.bnt_Scrapper = QPushButton(self.frame_top_menus)
        self.bnt_Scrapper.setMinimumSize(QSize(0, 60))
        font = QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        font.setBold(True)
        self.bnt_Scrapper.setFont(font)
        self.bnt_Scrapper.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 113, 165);\n"
"    border-radius: 10px ;\n"
"    margin: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        icon3 = QIcon()
        icon3.addPixmap(QPixmap("icons/binoculars-find-svgrepo-com.svg"), QIcon.Mode.Normal, QIcon.State.Off)
        self.bnt_Scrapper.setIcon(icon3)
        self.bnt_Scrapper.setIconSize(QSize(30, 30))
        self.bnt_Scrapper.setObjectName("bnt_Scrapper")
        self.verticalLayout_4.addWidget(self.bnt_Scrapper)
        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignmentFlag.AlignTop)
        self.horizontalLayout_2.addWidget(self.frame_left_menu)
        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setStyleSheet("background-color: rgb(219, 255, 253);\n"
"")
        self.frame_pages.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName("stackedWidget")
        self.learning = QWidget()
        self.learning.setObjectName("learning")
        self.verticalLayout_7 = QVBoxLayout(self.learning)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.scrollArea = QScrollArea(self.learning)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scroll_learning = QWidget()
        self.scroll_learning.setGeometry(QRect(0, 0, 81, 1000))
        self.scroll_learning.setObjectName("scroll_learning")
        self.verticalLayout_9 = QVBoxLayout(self.scroll_learning)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.fram_learning = QFrame(self.scroll_learning)
        self.fram_learning.setMinimumSize(QSize(0, 1000))
        self.fram_learning.setFrameShape(QFrame.Shape.StyledPanel)
        self.fram_learning.setFrameShadow(QFrame.Shadow.Raised)
        self.fram_learning.setObjectName("fram_learning")
        self.verticalLayout_10 = QVBoxLayout(self.fram_learning)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_9.addWidget(self.fram_learning)
        self.scrollArea.setWidget(self.scroll_learning)
        self.verticalLayout_7.addWidget(self.scrollArea)
        self.stackedWidget.addWidget(self.learning)
        self.visaulization = QWidget()
        self.visaulization.setObjectName("visaulization")
        self.verticalLayout_6 = QVBoxLayout(self.visaulization)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame = QFrame(self.visaulization)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 4px solid rgb(0, 0, 0);\n"
"    border-radius: 10px;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setMinimumSize(QSize(120, 50))
        font = QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(0, 113, 165);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px ;\n"
"    margin: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.verticalLayout_6.addWidget(self.frame)
        self.scrollArea_2 = QScrollArea(self.visaulization)
        self.scrollArea_2.setStyleSheet(" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {    \n"
"    background-color: rgb(80, 80, 122);\n"
"    min-height: 30px;\n"
"    border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{    \n"
"    background-color: rgb(0, 113, 165);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {    \n"
"    background-color: rgb(0, 113, 165);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(59, 59, 90);\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {    \n"
"    background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {    \n"
"    background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(59, 59, 90);\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {    \n"
"    background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {    \n"
"    background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scroll_visualization = QWidget()
        self.scroll_visualization.setGeometry(QRect(0, -56, 760, 3000))
        self.scroll_visualization.setMinimumSize(QSize(0, 3000))
        self.scroll_visualization.setStyleSheet("")
        self.scroll_visualization.setObjectName("scroll_visualization")
        self.verticalLayout_11 = QVBoxLayout(self.scroll_visualization)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_visualization = QFrame(self.scroll_visualization)
        self.frame_visualization.setMinimumSize(QSize(0, 0))
        self.frame_visualization.setMaximumSize(QSize(16777215, 16777215))
        self.frame_visualization.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_visualization.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_visualization.setObjectName("frame_visualization")
        self.verticalLayout_12 = QVBoxLayout(self.frame_visualization)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_like = QFrame(self.frame_visualization)
        self.frame_like.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_like.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_like.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_like.setObjectName("frame_like")
        self.verticalLayout_14 = QVBoxLayout(self.frame_like)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_page_like = QLabel(self.frame_like)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_page_like.sizePolicy().hasHeightForWidth())
        self.label_page_like.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(14)
        font.setBold(True)
        self.label_page_like.setFont(font)
        self.label_page_like.setStyleSheet("\n"
"border-radius: 5px;")
        self.label_page_like.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.label_page_like.setWordWrap(False)
        self.label_page_like.setObjectName("label_page_like")
        self.verticalLayout_14.addWidget(self.label_page_like, 0, Qt.AlignmentFlag.AlignTop)
        self.graph_page_like = QVBoxLayout()
        self.graph_page_like.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.graph_page_like.setContentsMargins(0, -1, -1, -1)
        self.graph_page_like.setSpacing(0)
        self.graph_page_like.setObjectName("graph_page_like")
        self.verticalLayout_14.addLayout(self.graph_page_like)
        self.verticalLayout_14.setStretch(0, 1)
        self.verticalLayout_14.setStretch(1, 9)
        self.verticalLayout_12.addWidget(self.frame_like)
        self.frame_gender = QFrame(self.frame_visualization)
        font = QFont()
        font.setFamily("Rockwell Condensed")
        self.frame_gender.setFont(font)
        self.frame_gender.setStyleSheet("background-color: rgb(173,216,230);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_gender.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_gender.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_gender.setObjectName("frame_gender")
        self.verticalLayout_13 = QVBoxLayout(self.frame_gender)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_page_gender = QLabel(self.frame_gender)
        font = QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(14)
        font.setBold(True)
        self.label_page_gender.setFont(font)
        self.label_page_gender.setStyleSheet("\n"
"border-radius: 5px;")
        self.label_page_gender.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_page_gender.setObjectName("label_page_gender")
        self.verticalLayout_13.addWidget(self.label_page_gender, 0, Qt.AlignmentFlag.AlignTop)
        self.graph_page_fan = QVBoxLayout()
        self.graph_page_fan.setObjectName("graph_page_fan")
        self.verticalLayout_13.addLayout(self.graph_page_fan)
        self.verticalLayout_13.setStretch(0, 1)
        self.verticalLayout_13.setStretch(1, 9)
        self.verticalLayout_12.addWidget(self.frame_gender)
        self.frame_age = QFrame(self.frame_visualization)
        self.frame_age.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_age.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_age.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_age.setObjectName("frame_age")
        self.verticalLayout_16 = QVBoxLayout(self.frame_age)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_page_age = QLabel(self.frame_age)
        font = QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(14)
        font.setBold(True)
        self.label_page_age.setFont(font)
        self.label_page_age.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_page_age.setObjectName("label_page_age")
        self.verticalLayout_16.addWidget(self.label_page_age)
        self.graph_page_age = QVBoxLayout()
        self.graph_page_age.setObjectName("graph_page_age")
        self.verticalLayout_16.addLayout(self.graph_page_age)
        self.verticalLayout_16.setStretch(0, 1)
        self.verticalLayout_16.setStretch(1, 9)
        self.verticalLayout_12.addWidget(self.frame_age)
        self.frame_location = QFrame(self.frame_visualization)
        self.frame_location.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_location.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_location.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_location.setObjectName("frame_location")
        self.verticalLayout_20 = QVBoxLayout(self.frame_location)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_page_location = QLabel(self.frame_location)
        font = QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(14)
        font.setBold(True)
        self.label_page_location.setFont(font)
        self.label_page_location.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_page_location.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_page_location.setObjectName("label_page_location")
        self.verticalLayout_20.addWidget(self.label_page_location, 0, Qt.AlignmentFlag.AlignTop)
        self.graph_page_location = QVBoxLayout()
        self.graph_page_location.setObjectName("graph_page_location")
        self.verticalLayout_20.addLayout(self.graph_page_location)
        self.verticalLayout_20.setStretch(0, 1)
        self.verticalLayout_20.setStretch(1, 9)
        self.verticalLayout_12.addWidget(self.frame_location)
        self.frame_reach = QFrame(self.frame_visualization)
        self.frame_reach.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_reach.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_reach.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_reach.setObjectName("frame_reach")
        self.verticalLayout_15 = QVBoxLayout(self.frame_reach)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label = QLabel(self.frame_reach)
        font = QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_15.addWidget(self.label, 0, Qt.AlignmentFlag.AlignVCenter)
        self.graph_page_map = QVBoxLayout()
        self.graph_page_map.setObjectName("graph_page_map")
        
        self.verticalLayout_15.addLayout(self.graph_page_map)
        self.verticalLayout_15.setStretch(0, 1)
        self.verticalLayout_15.setStretch(1, 94)
        self.verticalLayout_12.addWidget(self.frame_reach)
        self.verticalLayout_11.addWidget(self.frame_visualization)
        self.scrollArea_2.setWidget(self.scroll_visualization)
        self.verticalLayout_6.addWidget(self.scrollArea_2)
        self.stackedWidget.addWidget(self.visaulization)
        self.page_3 = QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_8 = QVBoxLayout(self.page_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.stackedWidget.addWidget(self.page_3)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.frame_pages)
        self.verticalLayout.addWidget(self.Content)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_Visualization.setText(_translate("MainWindow", "Visualization"))
        self.btn_learning.setText(_translate("MainWindow", "Learning "))
        self.bnt_Scrapper.setText(_translate("MainWindow", "Scraper "))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Input Token"))
        self.pushButton.setText(_translate("MainWindow", "Enter"))
        self.label_page_like.setText(_translate("MainWindow", "New Facebook Page Likes"))
        self.label_page_gender.setText(_translate("MainWindow", "Fan Gender"))
        self.label_page_age.setText(_translate("MainWindow", "Fan Age"))
        self.label_page_location.setText(_translate("MainWindow", "Fan Location"))
        self.label.setText(_translate("MainWindow", "Page reach"))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
