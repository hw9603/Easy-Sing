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
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        font = QtGui.QFont()
        font.setFamily("Arial")
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("QMainFrame { background-image: url(:background.jpeg) }")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.generateButton = QtWidgets.QPushButton(self.centralWidget)
        self.generateButton.setMinimumSize(QtCore.QSize(340, 160))
        self.generateButton.setStyleSheet("font: 36pt \"Arial\";")
        self.generateButton.setObjectName("generateButton")
        self.horizontalLayout.addWidget(self.generateButton, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.playButton = QtWidgets.QPushButton(self.centralWidget)
        self.playButton.setMinimumSize(QtCore.QSize(340, 160))
        self.playButton.setStyleSheet("font: 36pt \"Arial\";")
        self.playButton.setObjectName("playButton")
        self.horizontalLayout.addWidget(self.playButton, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.restartButton = QtWidgets.QPushButton(self.centralWidget)
        self.restartButton.setMinimumSize(QtCore.QSize(340, 160))
        self.restartButton.setStyleSheet("font: 75 36pt \"Arial\";")
        self.restartButton.setObjectName("restartButton")
        self.horizontalLayout_2.addWidget(self.restartButton, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.exitButton = QtWidgets.QPushButton(self.centralWidget)
        self.exitButton.setMinimumSize(QtCore.QSize(340, 160))
        self.exitButton.setStyleSheet("font: 75 36pt \"Arial\";")
        self.exitButton.setObjectName("exitButton")
        self.horizontalLayout_2.addWidget(self.exitButton, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(1, 2)
        MainWindow.setCentralWidget(self.centralWidget)

        Ui_MainWindow.retranslateUi(self, MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vocaloid"))
        self.generateButton.setText(_translate("MainWindow", "Generate Song"))
        self.playButton.setText(_translate("MainWindow", "Play"))
        self.restartButton.setText(_translate("MainWindow", "Restart"))
        self.exitButton.setText(_translate("MainWindow", "Exit"))

