from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import sys

import cv2
import Q1
import Q2
import Q3
import Q4


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(906, 402)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 40, 161, 271))
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 40, 141, 31))
        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 90, 141, 41))
        self.pushButton_3 = QPushButton(self.groupBox)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 150, 141, 31))
        self.pushButton_7 = QPushButton(self.groupBox)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(10, 200, 141, 41))
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(190, 40, 161, 271))
        self.pushButton_4 = QPushButton(self.groupBox_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(10, 40, 141, 31))
        self.pushButton_8 = QPushButton(self.groupBox_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(10, 110, 141, 31))
        self.pushButton_9 = QPushButton(self.groupBox_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(10, 180, 141, 31))
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(570, 40, 261, 281))
        self.pushButton_5 = QPushButton(self.groupBox_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(50, 40, 151, 31))
        self.pushButton_13 = QPushButton(self.groupBox_3)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(50, 90, 151, 31))
        self.pushButton_14 = QPushButton(self.groupBox_3)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(50, 140, 151, 31))
        self.pushButton_15 = QPushButton(self.groupBox_3)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(50, 190, 151, 31))
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(360, 40, 181, 271))
        self.pushButton_6 = QPushButton(self.groupBox_4)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(20, 40, 141, 31))
        self.pushButton_10 = QPushButton(self.groupBox_4)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(20, 90, 141, 31))
        self.pushButton_11 = QPushButton(self.groupBox_4)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(20, 140, 141, 31))
        self.pushButton_12 = QPushButton(self.groupBox_4)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(20, 190, 141, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 906, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"1. Image Processing", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"1.1 Load Image", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"1.2 Color seperation", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"1.3 Color Transformation", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"1.4 Blending", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"2  Image Smoothing", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"2.1 Median Filter", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"2.2 Gaussian blur", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"2.3 Bilateral Filter", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"4. Transforms", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"4.1 Resize", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"4.2 translation", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"4.3 scaling, rotation", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"4.4 sharing", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"3. Edge detection", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"3.1 Gaussian Blur", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"3.2 Sobel X", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"3.3 Sobel Y", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"3.4 Magnitude", None))
    # retranslateUi

class My_window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(My_window, self).__init__(parent)
        self.setupUi(self)
        self.initUI()
    def Q31(self):
        img = Q3.Gaussian_blur()
        Q3.imgshow('Gaussian', img)
    def Q32(self):
        img = Q3.Sobel_x()
        Q3.imgshow('Sobel_x', img)
    def Q33(self):
        img = Q3.Sobel_y()
        Q3.imgshow('Sobel_y', img)
    def Q34(self):
        img = Q3.Magnitude()
        Q3.imgshow('Magnitude', img)

    def initUI(self):
        self.pushButton.clicked.connect(Q1.loadimage)
        self.pushButton_2.clicked.connect(Q1.colorSep)
        self.pushButton_3.clicked.connect(Q1.color_transform)
        self.pushButton_7.clicked.connect(Q1.Blending)
        self.pushButton_4.clicked.connect(Q2.median)
        self.pushButton_8.clicked.connect(Q2.Gaussian)
        self.pushButton_9.clicked.connect(Q2.Bilateral)
        self.pushButton_6.clicked.connect(self.Q31)
        self.pushButton_10.clicked.connect(self.Q32)
        self.pushButton_11.clicked.connect(self.Q33)
        self.pushButton_12.clicked.connect(self.Q34)
        self.pushButton_5.clicked.connect(Q4.resize)
        self.pushButton_13.clicked.connect(Q4.translation)
        self.pushButton_14.clicked.connect(Q4.scaling)
        self.pushButton_15.clicked.connect(Q4.sharing)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = My_window()

    ui.show()
    sys.exit(app.exec_())
