# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/zihanli/program/498-Vocaloid/vocaloid/gui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 950)
        MainWindow.setMinimumSize(QtCore.QSize(1600, 950))
        MainWindow.setMaximumSize(QtCore.QSize(1600, 950))
        font = QtGui.QFont()
        font.setFamily("Arial")
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("QMainFrame { background-image: url(:background.jpeg) }")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(390, 170, 821, 131))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.tutorialButton = QtWidgets.QPushButton(self.centralWidget)
        self.tutorialButton.setGeometry(QtCore.QRect(400, 390, 401, 241))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tutorialButton.setFont(font)
        self.tutorialButton.setStyleSheet("font: 48pt \"Arial\";")
        self.tutorialButton.setObjectName("tutorialButton")
        self.startButton = QtWidgets.QPushButton(self.centralWidget)
        self.startButton.setGeometry(QtCore.QRect(800, 390, 401, 241))
        self.startButton.setStyleSheet("font: 48pt \"Arial\";")
        self.startButton.setObjectName("startButton")
        MainWindow.setCentralWidget(self.centralWidget)

        Ui_MainWindow.retranslateUi(self, MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vocaloid"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:84pt; color:#ffaa22;\">Welcome to Vocaloid!</span></p></body></html>"))
        self.tutorialButton.setText(_translate("MainWindow", "TUTORIAL"))
        self.startButton.setText(_translate("MainWindow", "START"))

