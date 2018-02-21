# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/hewen/Stuffs/Winter2018/EECS 498/EECS-498-Vocaloid/vocaloid/gui/generatewindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily("Arial")
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("QMainFrame { background-image: url(:background.jpeg) }")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.generateButton = QtWidgets.QPushButton(self.centralWidget)
        self.generateButton.setGeometry(QtCore.QRect(300, 120, 211, 71))
        self.generateButton.setStyleSheet("font: 24pt \"Arial\";")
        self.generateButton.setObjectName("generateButton")
        self.playButton = QtWidgets.QPushButton(self.centralWidget)
        self.playButton.setGeometry(QtCore.QRect(340, 300, 131, 71))
        self.playButton.setStyleSheet("font: 24pt \"Arial\";")
        self.playButton.setObjectName("playButton")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vocaloid"))
        self.generateButton.setText(_translate("MainWindow", "Generate Song"))
        self.playButton.setText(_translate("MainWindow", "Play!"))

