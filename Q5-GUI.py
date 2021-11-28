import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import Q5

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

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"VGG16", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Load data", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"print hyperparameter", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"print model", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"test", None))

class My_window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(My_window, self).__init__(parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(Q5.load_data)
        self.pushButton_2.clicked.connect(Q5.print_hyper)
        self.pushButton_3.clicked.connect(Q5.print_func)
        self.pushButton_7.clicked.connect(Q5.print_func)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = My_window()

    ui.show()
    sys.exit(app.exec_())