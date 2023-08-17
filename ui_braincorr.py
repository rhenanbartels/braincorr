# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'braincorr.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1400, 800)
        MainWindow.setMinimumSize(QSize(1400, 800))
        MainWindow.setStyleSheet(u"*{\n"
"	background-color:rgb(0,0,0)\n"
"}\n"
"QMenuBar{\n"
" 	background-color:rgb(100,100,100)\n"
"}\n"
"QMenuBar::item{\n"
" 	color:rgb(255,255,255)\n"
"}\n"
"QMenu{\n"
" 	color:rgb(255,255,255);\n"
"	background-color:rgb(100,100,100)\n"
"}")
        self.menu_file_open_action = QAction(MainWindow)
        self.menu_file_open_action.setObjectName(u"menu_file_open_action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_menu = QFrame(self.centralwidget)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setMinimumSize(QSize(250, 0))
        self.left_menu.setMaximumSize(QSize(250, 16777215))
        self.left_menu.setFrameShape(QFrame.StyledPanel)
        self.left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.left_menu)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")

        self.horizontalLayout.addWidget(self.left_menu)

        self.results_frame = QFrame(self.centralwidget)
        self.results_frame.setObjectName(u"results_frame")
        self.results_frame.setFrameShape(QFrame.StyledPanel)
        self.results_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.results_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.main_results_frame = QFrame(self.results_frame)
        self.main_results_frame.setObjectName(u"main_results_frame")
        self.main_results_frame.setFrameShape(QFrame.StyledPanel)
        self.main_results_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_results_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.main_results_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.top_plot = PlotWidget(self.frame_2)
        self.top_plot.setObjectName(u"top_plot")

        self.verticalLayout_5.addWidget(self.top_plot)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_5 = QFrame(self.main_results_frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.bottom_plot = PlotWidget(self.frame_5)
        self.bottom_plot.setObjectName(u"bottom_plot")

        self.verticalLayout_4.addWidget(self.bottom_plot)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.main_results_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 180))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 100))

        self.verticalLayout_3.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.frame_6)


        self.horizontalLayout_2.addWidget(self.main_results_frame)

        self.side_plots_frame = QFrame(self.results_frame)
        self.side_plots_frame.setObjectName(u"side_plots_frame")
        self.side_plots_frame.setMaximumSize(QSize(350, 16777215))
        self.side_plots_frame.setFrameShape(QFrame.StyledPanel)
        self.side_plots_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.side_plots_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.side_plots_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.side_top_plot = PlotWidget(self.frame_3)
        self.side_top_plot.setObjectName(u"side_top_plot")

        self.verticalLayout_7.addWidget(self.side_top_plot)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.side_plots_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.side_bottom_plot = PlotWidget(self.frame_4)
        self.side_bottom_plot.setObjectName(u"side_bottom_plot")

        self.verticalLayout_6.addWidget(self.side_bottom_plot)


        self.verticalLayout.addWidget(self.frame_4)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.side_plots_frame)


        self.horizontalLayout.addWidget(self.results_frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1400, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.menu_file_open_action)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PulseWave", None))
        self.menu_file_open_action.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Results:", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

