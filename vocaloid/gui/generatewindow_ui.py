# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/zihanli/program/498-Vocaloid/vocaloid/gui/generatewindow.ui'
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
        self.generateButton = QtWidgets.QPushButton(self.centralWidget)
        self.generateButton.setGeometry(QtCore.QRect(700, 130, 211, 71))
        self.generateButton.setStyleSheet("font: 24pt \"Arial\";")
        self.generateButton.setObjectName("generateButton")
        self.playButton = QtWidgets.QPushButton(self.centralWidget)
        self.playButton.setGeometry(QtCore.QRect(740, 340, 131, 71))
        self.playButton.setStyleSheet("font: 24pt \"Arial\";")
        self.playButton.setObjectName("playButton")
        MainWindow.setCentralWidget(self.centralWidget)

        Ui_MainWindow.retranslateUi(self, MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vocaloid"))
        self.generateButton.setText(_translate("MainWindow", "Generate Song"))
        self.playButton.setText(_translate("MainWindow", "Play!"))

