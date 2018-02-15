# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/hewen/Stuffs/Winter2018/EECS 498/EECS-498-Vocaloid/vocaloid/gui/myapp/gui/melodywindow.ui'
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
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(50, 140, 221, 71))
        self.label.setStyleSheet("font: 72pt \"ProFont for Powerline\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(50, 280, 251, 71))
        self.label_2.setStyleSheet("font: 72pt \"ProFont for Powerline\";")
        self.label_2.setObjectName("label_2")
        self.pitchLabel = QtWidgets.QLabel(self.centralWidget)
        self.pitchLabel.setGeometry(QtCore.QRect(380, 140, 381, 71))
        self.pitchLabel.setStyleSheet("font: 72pt \"ProFont for Powerline\";")
        self.pitchLabel.setText("")
        self.pitchLabel.setObjectName("pitchLabel")
        self.lengthLabel = QtWidgets.QLabel(self.centralWidget)
        self.lengthLabel.setGeometry(QtCore.QRect(380, 280, 381, 71))
        self.lengthLabel.setStyleSheet("font: 72pt \"ProFont for Powerline\";")
        self.lengthLabel.setText("")
        self.lengthLabel.setObjectName("lengthLabel")
        self.back2Button = QtWidgets.QPushButton(self.centralWidget)
        self.back2Button.setGeometry(QtCore.QRect(50, 450, 121, 61))
        self.back2Button.setStyleSheet("font: 36pt \"ProFont for Powerline\";")
        self.back2Button.setObjectName("back2Button")
        self.next2Button = QtWidgets.QPushButton(self.centralWidget)
        self.next2Button.setGeometry(QtCore.QRect(610, 450, 121, 61))
        self.next2Button.setStyleSheet("font: 36pt \"ProFont for Powerline\";")
        self.next2Button.setObjectName("next2Button")
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
        self.label.setText(_translate("MainWindow", "Pitch:"))
        self.label_2.setText(_translate("MainWindow", "Length:"))
        self.back2Button.setText(_translate("MainWindow", "BACK"))
        self.next2Button.setText(_translate("MainWindow", "NEXT"))

