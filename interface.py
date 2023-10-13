# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QRadioButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1500, 1000)
        MainWindow.setMinimumSize(QSize(1500, 1000))
        self.menu_file_open_action = QAction(MainWindow)
        self.menu_file_open_action.setObjectName(u"menu_file_open_action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(350, 0))
        self.frame.setMaximumSize(QSize(300, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 60))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEditFileName = QLineEdit(self.frame_6)
        self.lineEditFileName.setObjectName(u"lineEditFileName")
        self.lineEditFileName.setEnabled(False)
        self.lineEditFileName.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lineEditFileName)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 130))
        self.frame_7.setMaximumSize(QSize(16777215, 180))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_7)
        self.gridLayout.setObjectName(u"gridLayout")
        self.comboBox_2 = QComboBox(self.frame_7)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(116, 0))

        self.gridLayout.addWidget(self.comboBox_2, 3, 1, 1, 1)

        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 120))
        self.label_5.setFont(font)

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(105, 0))
        self.label_4.setMaximumSize(QSize(100, 16777215))
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_3 = QLabel(self.frame_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(181, 0))
        self.label_3.setMaximumSize(QSize(160, 16777215))
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 120))
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.comboBox = QComboBox(self.frame_7)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(116, 0))

        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.frame_7)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMaximumSize(QSize(40, 30))
        self.lineEdit_3.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_3, 1, 1, 1, 1)

        self.lineEdit_4 = QLineEdit(self.frame_7)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMaximumSize(QSize(40, 30))
        self.lineEdit_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_4, 2, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 130))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_8)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEditHFLower = QLineEdit(self.frame_8)
        self.lineEditHFLower.setObjectName(u"lineEditHFLower")
        self.lineEditHFLower.setMaximumSize(QSize(40, 30))
        self.lineEditHFLower.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEditHFLower, 3, 2, 1, 1)

        self.label_9 = QLabel(self.frame_8)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(10, 16777215))

        self.gridLayout_2.addWidget(self.label_9, 0, 3, 1, 1)

        self.label_7 = QLabel(self.frame_8)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 120))
        self.label_7.setFont(font)

        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)

        self.label_8 = QLabel(self.frame_8)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 120))
        self.label_8.setFont(font)

        self.gridLayout_2.addWidget(self.label_8, 3, 0, 1, 1)

        self.lineEditHFUpper = QLineEdit(self.frame_8)
        self.lineEditHFUpper.setObjectName(u"lineEditHFUpper")
        self.lineEditHFUpper.setMaximumSize(QSize(40, 30))
        self.lineEditHFUpper.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEditHFUpper, 3, 4, 1, 1)

        self.label_10 = QLabel(self.frame_8)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 2, 3, 1, 1)

        self.lineEditLFLower = QLineEdit(self.frame_8)
        self.lineEditLFLower.setObjectName(u"lineEditLFLower")
        self.lineEditLFLower.setMaximumSize(QSize(40, 30))
        self.lineEditLFLower.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEditLFLower, 2, 2, 1, 1)

        self.lineEditVLFUpper = QLineEdit(self.frame_8)
        self.lineEditVLFUpper.setObjectName(u"lineEditVLFUpper")
        self.lineEditVLFUpper.setMaximumSize(QSize(40, 30))
        self.lineEditVLFUpper.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEditVLFUpper, 0, 4, 1, 1)

        self.lineEditLFUpper = QLineEdit(self.frame_8)
        self.lineEditLFUpper.setObjectName(u"lineEditLFUpper")
        self.lineEditLFUpper.setMaximumSize(QSize(40, 30))
        self.lineEditLFUpper.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEditLFUpper, 2, 4, 1, 1)

        self.label_12 = QLabel(self.frame_8)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 3, 3, 1, 1)

        self.lineEditVLFLower = QLineEdit(self.frame_8)
        self.lineEditVLFLower.setObjectName(u"lineEditVLFLower")
        self.lineEditVLFLower.setMaximumSize(QSize(40, 30))
        self.lineEditVLFLower.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEditVLFLower, 0, 2, 1, 1)

        self.label_6 = QLabel(self.frame_8)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(80, 120))
        self.label_6.setFont(font)

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_8)

        self.frame_10 = QFrame(self.frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 89))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_10)
        self.formLayout.setObjectName(u"formLayout")
        self.label_14 = QLabel(self.frame_10)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(180, 0))
        self.label_14.setMaximumSize(QSize(170, 16777215))
        self.label_14.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_14)

        self.lineEdit_11 = QLineEdit(self.frame_10)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setMaximumSize(QSize(40, 30))
        self.lineEdit_11.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_11)

        self.label_15 = QLabel(self.frame_10)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(16777215, 120))
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(u"#label_15{\n"
"	margin-top:10px\n"
"}")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_15)

        self.radioButtonApplyCoherence = QRadioButton(self.frame_10)
        self.radioButtonApplyCoherence.setObjectName(u"radioButtonApplyCoherence")
        self.radioButtonApplyCoherence.setMaximumSize(QSize(40, 16777215))
        self.radioButtonApplyCoherence.setStyleSheet(u"#radioButtonApplyCoherence {\n"
"	margin-top: 15px;\n"
"   padding-left:12px;\n"
"  margin-bottom:2px;\n"
"}")
        self.radioButtonApplyCoherence.setChecked(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.radioButtonApplyCoherence)


        self.verticalLayout_2.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 180))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_11)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_16 = QLabel(self.frame_11)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(180, 0))
        self.label_16.setMaximumSize(QSize(170, 16777215))
        self.label_16.setFont(font)

        self.gridLayout_4.addWidget(self.label_16, 0, 0, 1, 1)

        self.comboBox_3 = QComboBox(self.frame_11)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMinimumSize(QSize(200, 30))
        self.comboBox_3.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_4.addWidget(self.comboBox_3, 0, 1, 1, 3)

        self.label_17 = QLabel(self.frame_11)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(123, 0))
        self.label_17.setMaximumSize(QSize(170, 16777210))
        self.label_17.setFont(font)

        self.gridLayout_4.addWidget(self.label_17, 1, 0, 1, 1)

        self.comboBox_4 = QComboBox(self.frame_11)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setMinimumSize(QSize(200, 30))
        self.comboBox_4.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_4.addWidget(self.comboBox_4, 1, 1, 1, 3)

        self.label_19 = QLabel(self.frame_11)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(62, 16777215))

        self.gridLayout_4.addWidget(self.label_19, 2, 0, 1, 1)

        self.lineEditStartTimeAxes = QLineEdit(self.frame_11)
        self.lineEditStartTimeAxes.setObjectName(u"lineEditStartTimeAxes")
        self.lineEditStartTimeAxes.setMinimumSize(QSize(70, 0))
        self.lineEditStartTimeAxes.setMaximumSize(QSize(50, 30))
        self.lineEditStartTimeAxes.setLayoutDirection(Qt.LeftToRight)
        self.lineEditStartTimeAxes.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lineEditStartTimeAxes, 2, 1, 1, 1)

        self.label_18 = QLabel(self.frame_11)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(10, 0))
        self.label_18.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_18, 2, 2, 1, 1)

        self.lineEditEndTimeAxes = QLineEdit(self.frame_11)
        self.lineEditEndTimeAxes.setObjectName(u"lineEditEndTimeAxes")
        self.lineEditEndTimeAxes.setMinimumSize(QSize(70, 0))
        self.lineEditEndTimeAxes.setMaximumSize(QSize(50, 30))
        self.lineEditEndTimeAxes.setLayoutDirection(Qt.LeftToRight)
        self.lineEditEndTimeAxes.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lineEditEndTimeAxes, 2, 3, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_11)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_9 = QFrame(self.frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 40))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.statusEdit = QLineEdit(self.frame_9)
        self.statusEdit.setObjectName(u"statusEdit")
        self.statusEdit.setEnabled(False)
        self.statusEdit.setMaximumSize(QSize(14, 14))
        self.statusEdit.setStyleSheet(u"#statusEdit {\n"
"	background-color: rgb(0,255,0); \n"
"	color: rgb(0,255,0);\n"
"	border-radius: 4px\n"
"}")

        self.horizontalLayout_3.addWidget(self.statusEdit)

        self.label_13 = QLabel(self.frame_9)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 14))
        self.label_13.setMaximumSize(QSize(300, 15))

        self.horizontalLayout_3.addWidget(self.label_13)


        self.verticalLayout_2.addWidget(self.frame_9)


        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.top_plot = PlotWidget(self.frame_3)
        self.top_plot.setObjectName(u"top_plot")

        self.verticalLayout_5.addWidget(self.top_plot)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.bottom_plot = PlotWidget(self.frame_4)
        self.bottom_plot.setObjectName(u"bottom_plot")

        self.verticalLayout_4.addWidget(self.bottom_plot)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 150))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_11 = QLabel(self.frame_5)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_3.addWidget(self.label_11)


        self.verticalLayout.addWidget(self.frame_5)


        self.gridLayout_3.addWidget(self.frame_2, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1500, 19))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.menu_file_open_action)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu_file_open_action.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Filename:", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Hanning", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Hamming", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Rectangular", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"-", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Window:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Zero Padding::", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Resampling Frequency:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Interp. Method:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Linear", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Cubic spline", None))

        self.lineEdit_3.setInputMask(QCoreApplication.translate("MainWindow", u"00", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.lineEdit_4.setInputMask(QCoreApplication.translate("MainWindow", u"000", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEditHFLower.setInputMask(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.lineEditHFLower.setText(QCoreApplication.translate("MainWindow", u"0.2", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">LF </span><span style=\" font-weight:700; vertical-align:sub;\">(Hz)</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>HF <span style=\" vertical-align:sub;\">(Hz)</span></p></body></html>", None))
        self.lineEditHFUpper.setInputMask(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.lineEditHFUpper.setText(QCoreApplication.translate("MainWindow", u"0.5", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.lineEditLFLower.setInputMask(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.lineEditLFLower.setText(QCoreApplication.translate("MainWindow", u"0.07", None))
        self.lineEditVLFUpper.setInputMask(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.lineEditVLFUpper.setText(QCoreApplication.translate("MainWindow", u"0.07", None))
        self.lineEditLFUpper.setInputMask(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.lineEditLFUpper.setText(QCoreApplication.translate("MainWindow", u"0.2", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.lineEditVLFLower.setInputMask(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.lineEditVLFLower.setText(QCoreApplication.translate("MainWindow", u"0.02", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">VLF</span><span style=\" font-weight:700; vertical-align:sub;\"> (Hz)</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Coherence Threshold:", None))
        self.lineEdit_11.setInputMask(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.lineEdit_11.setText(QCoreApplication.translate("MainWindow", u"0.5", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Apply threshold:", None))
        self.radioButtonApplyCoherence.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Top Axes:", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"CBV - Signal", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"CBV - PSD", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Gain", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"Coherence", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("MainWindow", u"Phase", None))

        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Bottom Axes:", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"ABP - Signal", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"ABP - PSD", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"Gain", None))
        self.comboBox_4.setItemText(3, QCoreApplication.translate("MainWindow", u"Coherence", None))
        self.comboBox_4.setItemText(4, QCoreApplication.translate("MainWindow", u"Phase", None))

        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Time </span><span style=\" font-weight:700; vertical-align:sub;\">(s)</span><span style=\" font-weight:700;\">:</span></p></body></html>", None))
        self.lineEditStartTimeAxes.setInputMask(QCoreApplication.translate("MainWindow", u"00000.00", None))
        self.lineEditStartTimeAxes.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.lineEditEndTimeAxes.setInputMask(QCoreApplication.translate("MainWindow", u"00000.00", None))
        self.lineEditEndTimeAxes.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Ready", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Results", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

