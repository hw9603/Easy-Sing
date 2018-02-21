# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/hewen/Stuffs/Winter2018/EECS 498/EECS-498-Vocaloid/vocaloid/gui/mainwindow.ui'
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
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(110, 150, 641, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.tutorialButton = QtWidgets.QPushButton(self.centralWidget)
        self.tutorialButton.setGeometry(QtCore.QRect(160, 360, 211, 71))
        self.tutorialButton.setStyleSheet("font: 36pt \"Arial\";")
        self.tutorialButton.setObjectName("tutorialButton")
        self.startButton = QtWidgets.QPushButton(self.centralWidget)
        self.startButton.setGeometry(QtCore.QRect(470, 360, 161, 71))
        self.startButton.setStyleSheet("font: 36pt \"Arial\";")
        self.startButton.setObjectName("startButton")
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:64pt; color:#2a466f;\">Welcome to Vocaloid!</span></p></body></html>"))
        self.tutorialButton.setText(_translate("MainWindow", "TUTORIAL"))
        self.startButton.setText(_translate("MainWindow", "START"))

