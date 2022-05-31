
from os import remove
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import PySide2.QtWebEngineWidgets as QtWebEngine
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import io

# GUI FILE
from ui_main import Ui_MainWindow
from data import LoadData
# IMPORT FUNCTIONS
from ui_functions import *
import mplcursors
import folium

GLOBAL_DATA = LoadData()

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        

        ## TOGGLE/BURGUER MENU

        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))

        ## PAGES
     

        # PAGE 1
        self.ui.btn_learning.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.learning))

        # PAGE 2
        self.ui.btn_Visualization.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.visaulization))

        # PAGE 3
        self.ui.bnt_Scrapper.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))

        self.tokenInputTextEdit = self.ui.lineEdit
        self.ui.pushButton.clicked.connect(self.button_click)
        self.show()

    def reloadGraphs(self):
        ## SHOW ==> MAIN WINDOW
        
        self.page_like = Canvas_like()
        self.page_gender = Canvas_gender()
        self.graph_page_location = Canvas_location()
        self.graph_page_age = Canvas_age()
        self.graph_map = Canvas_map()

        self.ui.graph_page_like.addWidget(self.page_like)
        self.ui.graph_page_fan.addWidget(self.page_gender)
        self.ui.graph_page_location.addWidget(self.graph_page_location)
        self.ui.graph_page_age.addWidget(self.graph_page_age)
        # add QT Web Engine
        self.view = QtWebEngine.QWebEngineView()
        self.view.setHtml.setSource(QtCore.QUrl.fromLocalFile("map.html"))
        self.ui.graph_page_map.addWidget(self.view)
        
        # self.ui.grafica_cuatro.addWidget(self.page_top)
        


    def button_click(self):
        # shost is a QString object
        token = self.tokenInputTextEdit.text()
        GLOBAL_DATA.setToken(token= token)
        
        self.reloadGraphs()
        

class Canvas_map():
    def __init__(self):
        city = GLOBAL_DATA.get_location()
        lat_long = GLOBAL_DATA.get_lat_long()


        lat = lat_long[0][0]
        long = lat_long[0][1]
    
        m = folium.Map(location=[lat_long[0][0], lat_long[1][0]])
        

        for x in range(len(lat_long[0])):
            tooltip = str(city[0][x]) + ":" + str(city[1][x])
            folium.Marker(
                [lat_long[0][x], lat_long[1][x]], 
                popup="<i>" + str(city[2][x]) +"%"+ "</i>", 
                tooltip=tooltip, 
                icon= folium.Icon(color='darkblue', icon="user")
        ).add_to(m)
        m
        m.save("map.html")
        self.map_data = io.BytesIO()
        m.save(self.map_data, close_file=False)
        
    def getMapData(self):
        return self.map_data
class Canvas_like(FigureCanvas):
    def __init__(self, parent=None ):     
        self.fig, self.ax = plt.subplots(figsize =(16, 14))
        super().__init__(self.fig) 
        likes= GLOBAL_DATA.get_like()
        x = likes[0]
        y = likes[1]

        removed = GLOBAL_DATA.get_removed()
        x1 = removed[0]
        y1 = removed[1]

        # ax = plt.gca()
        print(x,y)
        print(len(x),len(y))
        self.ax.plot(x, y,color = "green", linestyle="-",marker="o", label='New Fans')
        self.ax.plot(x1, y1,color ="red", linestyle="-", marker="o", label='Removed Fans')

        self.ax.legend()
        self.ax.set_xticklabels (x,rotation = 45)
        # self.ax.set_xticklabels(x, rotation = 45)
        # mplcursors.cursor(hover=True)
        # self.fig.suptitle('Page Like',size=9)
        
        for s in ['top', 'bottom', 'left', 'right']:
            self.ax.spines[s].set_visible(False)

        # Remove x, y Ticks
        self.ax.xaxis.set_ticks_position('none')
        self.ax.yaxis.set_ticks_position('none')

        # Add padding between axes and labels
        self.ax.xaxis.set_tick_params(pad = 20)
        self.ax.yaxis.set_tick_params(pad = 0)

        # Add x, y gridlines
        self.ax.grid(b = True, color ='grey',
                linestyle ='-.', linewidth = 0.5,
                alpha = 0.2)
        self.ax.set_title('page New Fans like',loc ='left',fontweight ='bold' )

class Canvas_gender(FigureCanvas):
    def __init__(self, parent=None):     
        self.fig, self.ax = plt.subplots(figsize =(15, 9))
        super().__init__(self.fig) 

        m = GLOBAL_DATA.get_gender()[0]
        f = GLOBAL_DATA.get_gender()[1]
        u = GLOBAL_DATA.get_gender()[2]

        number = ['M', 'F', 'U']
        colores = ['cyan','pink','yellow']
        value = [m, f,u]
        explotar = [0.05, 0.05, 0.05] 

        plt.title("Graph Fan Gender",
            color='black', family="Arial",fontweight ='bold')

        self.ax.pie(value, explode = explotar, labels = number, 
            colors = colores,
                autopct = '%.02f%%', pctdistance = 0.6,
                shadow=True, startangle=90, radius = 0.8, 
                labeldistance=1.1)  
        # mplcursors.cursor(hover=True)
        self.ax.axis('equal')




class Canvas_location(FigureCanvas):
    def __init__(self, parent=None):     
        self.fig, self.ax = plt.subplots(figsize =(16, 15))
        super().__init__(self.fig) 
        data= GLOBAL_DATA.get_location()
        x = data[0]
        y = data[1]


        # Horizontal Bar Plot
        self.ax.barh(x, y)
        # Remove axes splines
        for s in ['top', 'bottom', 'left', 'right']:
            self.ax.spines[s].set_visible(False)

        # Remove x, y Ticks
        self.ax.xaxis.set_ticks_position('none')
        self.ax.yaxis.set_ticks_position('none')

        # Add padding between axes and labels
        self.ax.xaxis.set_tick_params(pad = 20)
        self.ax.yaxis.set_tick_params(pad = 0)

        # Add x, y gridlines
        self.ax.grid(b = True, color ='grey',
                linestyle ='-.', linewidth = 0.5,
                alpha = 0.2)

        # Add annotation to bars
        for i in self.ax.patches:
            plt.text(i.get_width()+0.2, i.get_y()+0.5,
                    str(round((i.get_width()), 20)),
                    fontsize = 8, fontweight ='bold',
                    color ='grey')

        # Add Plot Title
        self.ax.set_title('Page Fans Location',
                    loc ='right',fontweight ='bold' )
        # mplcursors.cursor(hover=True)

        
class Canvas_age(FigureCanvas):
    def __init__(self, parent=None):     
        self.fig, self.ax = plt.subplots(figsize =(16, 12))
        super().__init__(self.fig) 
        data= GLOBAL_DATA.get_gender_age()
        x = data[0]
        y = data[1]


        # Horizontal Bar Plot
        self.ax.bar(x, y)
        # Remove axes splines
        for s in ['top', 'bottom', 'left', 'right']:
            self.ax.spines[s].set_visible(False)

        # Remove x, y Ticks
        self.ax.xaxis.set_ticks_position('none')
        self.ax.yaxis.set_ticks_position('none')

        # Add padding between axes and labels
        self.ax.xaxis.set_tick_params(pad = 20)
        self.ax.yaxis.set_tick_params(pad = 0)

        # Add x, y gridlines
        self.ax.grid(b = True, color ='grey',
                linestyle ='-.', linewidth = 0.5,
                alpha = 0.2)

        # Add annotation to bars
        for i in self.ax.patches:
            plt.text(i.get_width()+0.2, i.get_y()+0.5,
                    str(round((i.get_width()), 10)),
                    fontsize = 8, fontweight ='bold',
                    color ='grey')

        # Add Plot Title
        self.ax.set_title('Gender : Age Ratio',
                    loc ='center',fontweight ='bold' )
        # mplcursors.cursor(hover=True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
